# from typing import ForwardRef, NewType, TypeAlias, Optional
from typing import Literal
from bson import DBRef
from beanie import BackLink, Document, WriteRules, after_event, Insert, Link, PydanticObjectId  # BackLink
from fastapi_users_db_beanie import BeanieBaseUser
from pydantic import Field
from unipoll_api.utils import colored_dbg as Debug
from unipoll_api.utils.token_db import BeanieBaseAccessToken


# Create a link to the Document model
async def create_link(document: Document) -> Link:
    ref = DBRef(collection=document._document_settings.name,  # type: ignore
                id=document.id)
    link = Link(ref, type(document))
    return link


# Custom PydanticObjectId class to override due to a bug
class ResourceID(PydanticObjectId):
    @classmethod
    def __modify_schema__(cls, field_schema):  # type: ignore
        field_schema.update(
            type="string",
            example="5eb7cf5a86d9755df3a6c593",
        )


class AccessToken(BeanieBaseAccessToken, Document):  # type: ignore
    pass


class Resource(Document):
    id: ResourceID = Field(default_factory=ResourceID, alias="_id")
    resource_type: Literal["workspace", "group", "poll"]
    name: str = Field(
        title="Name", description="Name of the resource", min_length=3, max_length=50)
    description: str = Field(default="", title="Description", max_length=1000)
    policies: list[Link["Policy"]] = []

    @after_event(Insert)
    def create_group(self) -> None:
        Debug.info(f'New {self.resource_type} "{self.id}" has been created')

    async def add_policy(self, member: "Group | Account", permissions, save: bool = True) -> None:
        new_policy = Policy(policy_holder_type='account',
                            policy_holder=(await create_link(member)),
                            permissions=permissions,
                            parent_resource=(await create_link(self)))  # type: ignore

        # Add the policy to the group
        self.policies.append(new_policy)  # type: ignore
        if save:
            await self.save(link_rule=WriteRules.WRITE)  # type: ignore

    async def remove_policy(self, policy: "Policy", save: bool = True) -> None:
        for i, p in enumerate(self.policies):
            if policy.id == p.ref.id:
                self.policies.remove(p)
                if save:
                    await self.save(link_rule=WriteRules.WRITE)  # type: ignore

    async def remove_member_policy(self, member: "Group | Account", save: bool = True) -> None:
        for policy in self.policies:
            if policy.policy_holder.ref.id == member.id:  # type: ignore
                self.policies.remove(policy)
                if save:
                    await self.save(link_rule=WriteRules.WRITE)  # type: ignore


class Account(BeanieBaseUser, Document):  # type: ignore
    id: ResourceID = Field(default_factory=ResourceID, alias="_id")
    first_name: str = Field(
        default_factory=str,
        max_length=20,
        min_length=2,
        pattern="^[A-Z][a-z]*$")
    last_name: str = Field(
        default_factory=str,
        max_length=20,
        min_length=2,
        pattern="^[A-Z][a-z]*$")


class Workspace(Resource):
    resource_type: Literal["workspace"] = "workspace"
    members: list[Link["Account"]] = []
    groups: list[Link["Group"]] = []
    polls: list[Link["Poll"]] = []

    async def add_member(self, account: "Account", permissions, save: bool = True) -> "Account":
        # Add the account to the group
        self.members.append(account)  # type: ignore
        # Create a policy for the new member
        await self.add_policy(account, permissions, save=False)  # type: ignore
        if save:
            await self.save(link_rule=WriteRules.WRITE)  # type: ignore
        return account

    async def remove_member(self, account, save: bool = True) -> bool:
        # Remove the account from the group
        for i, member in enumerate(self.members):
            if account.id == member.id:  # type: ignore
                self.members.remove(member)
                # type: ignore
                Debug.info(f"Removed member {member.id} from {self.resource_type} {self.id}")  # type: ignore
                break

        # Remove the policy from the workspace
        await self.remove_member_policy(account, save=False)  # type: ignore

        # Remove the member from all groups in the workspace
        group: Group
        for group in self.groups:  # type: ignore
            await group.remove_member(account, save=False)
            await group.remove_member_policy(account, save=False)
            await Group.save(group, link_rule=WriteRules.WRITE)

        if save:
            await self.save(link_rule=WriteRules.WRITE)  # type: ignore
        return True


class Group(Resource):
    resource_type: Literal["group"] = "group"
    workspace: BackLink[Workspace] = Field(original_field="groups")
    members: list[Link["Account"]] = []
    groups: list[Link["Group"]] = []

    async def add_member(self, account: "Account", permissions, save: bool = True) -> "Account":
        if account not in self.workspace.members:  # type: ignore
            from unipoll_api.exceptions import WorkspaceExceptions
            raise WorkspaceExceptions.UserNotMember(
                self.workspace, account)  # type: ignore

        # Add the account to the group
        self.members.append(account)  # type: ignore
        # Create a policy for the new member
        await self.add_policy(account, permissions, save=False)  # type: ignore
        if save:
            await self.save(link_rule=WriteRules.WRITE)  # type: ignore
        return account

    async def remove_member(self, account, save: bool = True) -> bool:
        # Remove the account from the group
        for i, member in enumerate(self.members):
            if account.id == member.id:  # type: ignore
                self.members.remove(member)
                # type: ignore
                Debug.info(
                    f"Removed member {member.id} from {self.resource_type} {self.id}")  # type: ignore
                break

        # Remove the policy from the group
        await self.remove_member_policy(account, save=False)  # type: ignore

        if save:
            await self.save(link_rule=WriteRules.WRITE)  # type: ignore
        return True


class Poll(Resource):
    id: ResourceID = Field(default_factory=ResourceID, alias="_id")
    workspace: Link[Workspace]
    resource_type: Literal["poll"] = "poll"
    public: bool
    published: bool
    questions: list
    policies: list[Link["Policy"]]


class Policy(Document):
    id: ResourceID = Field(default_factory=ResourceID, alias="_id")
    parent_resource: Link[Workspace] | Link[Group] | Link[Poll]
    policy_holder_type: Literal["account", "group"]
    policy_holder: Link["Group"] | Link["Account"]
    permissions: int

    async def get_parent_resource(self, fetch_links: bool = False) -> Workspace | Group | Poll:
        from unipoll_api.exceptions.resource import ResourceNotFound
        collection = eval(self.parent_resource.ref.collection)
        parent: Workspace | Group | Poll = await collection.get(self.parent_resource.ref.id,
                                                                fetch_links=fetch_links)
        if not parent:
            ResourceNotFound(self.parent_resource.ref.collection,
                             self.parent_resource.ref.id)
        return parent

    async def get_policy_holder(self, fetch_links: bool = False) -> Group | Account:
        from unipoll_api.exceptions.policy import PolicyHolderNotFound
        collection = eval(self.policy_holder.ref.collection)
        policy_holder: Group | Account = await collection.get(self.policy_holder.ref.id,
                                                              fetch_links=fetch_links)
        if not policy_holder:
            PolicyHolderNotFound(self.policy_holder.ref.id)
        return policy_holder
