import typing as t
from enum import Enum
from datetime import datetime
from dataclasses import dataclass

from pydantic import BaseModel

from getajob.config.settings import SETTINGS
from getajob.vendor.firestore.repository import FirestoreDB
from getajob.vendor.kafka.repository import KafkaProducerRepository
from getajob.vendor.kafka.models import KafkaEventConfig


DataSchema = t.TypeVar("DataSchema", bound=BaseModel)


class BaseDataModel(BaseModel):
    id: str
    created: datetime
    updated: datetime | None = None


@dataclass
class PaginatedRequest:
    last: dict | None = None
    limit: int = SETTINGS.DEFAULT_PAGE_LIMIT


@dataclass
class PaginatedResponse:
    next: dict | None
    data: list[t.Any]


class Entity(str, Enum):
    USERS = "users"  # Comes from clerk
    USER_DETAILS = "user_details"  # What we add to user data
    USER_MEMBERSHIPS = "user_memberships"
    USER_SAVED_JOBS = "user_saved_jobs"
    USER_DASHBOARD = "user_dashboard"
    CHAT = "chat"
    CHAT_MESSAGES = "chat_messages"
    SKILLS = "skills"
    COVER_LETTERS = "cover_letters"
    RESUMES = "resumes"
    RESUME_EXTRACTED_DATA = "resume_extracted_data"
    COMPANIES = "companies"  # Comes from clerk
    COMPANY_DETAILS = "company_details"  # What we add to company data
    COMPANY_DASHBOARD = "company_dashboard"
    COMPANY_ATS_CONFIG = "company_ats_config"
    COMPANY_AUDITS = "company_audits"
    COMPANY_SAVES_CANDIDATES = "company_saves_candidates"
    RECRUITERS = "recruiters"  # Comes from clerk
    RECRUITER_INVITATIONS = "recruiter_invitations"  # Comes from clerk
    RECRUITER_DETAILS = "recruiter_details"  # What we add to recruiter data
    JOBS = "jobs"
    JOB_TEMPLATES = "job_templates"
    APPLICATIONS = "applications"
    APPLICATION_TRACKING = "application_tracking"
    USER_NOTIFICATIONS = "user_notifications"
    SCHEDULED_EVENTS = "scheduled_events"

    # Admin entities
    ADMIN_USERS = "admin_users"
    ADMIN_JOB_APPROVALS = "admin_job_approvals"


class Location(BaseModel):
    address_line_1: str
    address_line_2: str | None = None
    city: str
    state: str
    zipcode: str
    country: str
    lat: float
    lon: float


class RepositoryDependencies(BaseModel):
    user_id: str
    db: FirestoreDB
    collection_name: str
    entity_model: t.Type[BaseModel]
    kafka: t.Optional[KafkaProducerRepository] = None
    kafka_event_config: t.Optional[KafkaEventConfig] = None

    class Config:
        arbitrary_types_allowed = True


class UserAndDatabaseConnection(BaseModel):
    """Created during a request"""

    initiating_user_id: str
    db: FirestoreDB

    class Config:
        arbitrary_types_allowed = True


class ProcessedAsyncMessage(BaseModel):
    request_scope: UserAndDatabaseConnection
    object_id: str
    parent_collections: dict
    data: dict[str, t.Any] | BaseModel
