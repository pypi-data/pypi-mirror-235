from enum import Enum
from pydantic import BaseModel

from getajob.abstractions.models import BaseDataModel


class AdminRoles(str, Enum):
    admin = "admin"
    member = "member"
    read_only = "read_only"


class UserCreateAdminUser(BaseModel):
    user_email: str
    role: AdminRoles


class CreateAdminUser(UserCreateAdminUser):
    user_id: str


class AdminUser(BaseDataModel, CreateAdminUser):
    ...
