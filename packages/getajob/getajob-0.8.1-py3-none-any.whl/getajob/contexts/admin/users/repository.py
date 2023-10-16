from getajob.abstractions.repository import ParentRepository, RepositoryDependencies
from getajob.abstractions.models import Entity, UserAndDatabaseConnection
from getajob.contexts.users.repository import UserRepository
from getajob.exceptions import EntityNotFound

from .models import AdminUser, UserCreateAdminUser, CreateAdminUser


class AdminUserRepository(ParentRepository[AdminUser]):
    def __init__(self, *, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                user_id=request_scope.initiating_user_id,
                db=request_scope.db,
                collection_name=Entity.ADMIN_USERS.value,
                entity_model=AdminUser,
            ),
        )
        self.request_scope = request_scope

    def create(self, new_user: UserCreateAdminUser):
        # Get user
        user = UserRepository(
            request_scope=self.request_scope, kafka=None
        ).get_user_by_email(email=new_user.user_email)
        if user is None:
            raise EntityNotFound(f"User with email {new_user.user_email} not found")

        # Override to always use the provided user_id
        return super().create(
            CreateAdminUser(
                user_id=user.id,
                user_email=new_user.user_email,
                role=new_user.role,
            ),
            provided_id=user.id,
        )
