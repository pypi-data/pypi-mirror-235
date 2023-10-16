from pydantic import BaseModel

from getajob.abstractions.models import BaseDataModel


class SetRecruiterDetails(BaseModel):
    send_daily_updates: bool | None = None
    send_weekly_updates: bool | None = None
    send_new_application_updates: bool | None = None
    send_email_message_updates: bool | None = None


class CreateRecruiterDetails(SetRecruiterDetails):
    company_id: str
    user_id: str


class RecruiterDetails(CreateRecruiterDetails, BaseDataModel):
    ...
