from getajob.abstractions.repository import ParentRepository, RepositoryDependencies
from getajob.vendor.kafka.repository import KafkaProducerRepository
from getajob.vendor.kafka.models import (
    KafkaEventConfig,
    KafkaTopic,
    KafkaJobApprovalEnum,
)
from getajob.abstractions.models import Entity, UserAndDatabaseConnection
from getajob.contexts.admin.users.repository import AdminUserRepository

from .models import AdminJobPostApproval, UserCreateApprovalUpdate
from .unit_of_work import JobApprovalUnitOfWork


class AdminJobApprovalRepository(ParentRepository[AdminJobPostApproval]):
    def __init__(
        self,
        *,
        request_scope: UserAndDatabaseConnection,
        kafka: KafkaProducerRepository | None
    ):
        kafka_event_config = KafkaEventConfig(
            topic=KafkaTopic.jobs, message_type_enum=KafkaJobApprovalEnum
        )
        super().__init__(
            RepositoryDependencies(
                user_id=request_scope.initiating_user_id,
                db=request_scope.db,
                collection_name=Entity.ADMIN_JOB_APPROVALS.value,
                entity_model=AdminJobPostApproval,
                kafka=kafka,
                kafka_event_config=kafka_event_config,
            ),
        )
        self.admin_user_repo = AdminUserRepository(request_scope=request_scope)

    def update_job_approval_post(
        self, approval_id: str, admin_id: str, updates: UserCreateApprovalUpdate
    ):
        return JobApprovalUnitOfWork(
            approval_repo=self,
            admin_user_repo=self.admin_user_repo,
        ).update_job_approval_status(
            approval_id=approval_id,
            admin_id=admin_id,
            updates=updates,
        )
