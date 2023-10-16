from enum import Enum
from pydantic import BaseModel, Field

from getajob.abstractions.models import BaseDataModel


class ApprovalStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class CreateAdminJobPostApproval(BaseModel):
    company_id: str
    job_id: str
    requesting_user: str


class UserCreateApprovalUpdate(BaseModel):
    approval_status: ApprovalStatus
    reason: str


class UpdateApprovalStatus(UserCreateApprovalUpdate):
    approved_by_id: str
    approved_by_email: str


class AdminJobPostApproval(BaseDataModel, CreateAdminJobPostApproval):
    approval_status: ApprovalStatus = ApprovalStatus.PENDING
    history: list[UpdateApprovalStatus] = Field(default_factory=list)
