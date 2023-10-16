from getajob.abstractions.repository import BaseRepository

from .models import UpdateApprovalStatus, UserCreateApprovalUpdate, AdminJobPostApproval


class JobApprovalUnitOfWork:
    def __init__(
        self,
        approval_repo: BaseRepository,
        admin_user_repo: BaseRepository,
    ):
        self.approval_repo = approval_repo
        self.admin_user_repo = admin_user_repo

    def update_job_approval_status(
        self, approval_id: str, admin_id: str, updates: UserCreateApprovalUpdate
    ) -> AdminJobPostApproval:
        # Get admin information
        approving_admin = self.admin_user_repo.get(admin_id)

        # Define new status update
        status_update = UpdateApprovalStatus(
            approval_status=updates.approval_status,
            reason=updates.reason,
            approved_by_id=approving_admin.id,
            approved_by_email=approving_admin.user_email,
        )

        # Update approval status
        approval_object: AdminJobPostApproval = self.approval_repo.get(approval_id)
        approval_object.approval_status = updates.approval_status
        approval_object.history.append(status_update)
        self.approval_repo.update(approval_id, approval_object)
        return approval_object
