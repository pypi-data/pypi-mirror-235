from datetime import datetime

from pydantic import BaseModel
from hubspot.crm.contacts import SimplePublicObjectInputForCreate


class HubspotModel(BaseModel):
    def to_hubspot(self):
        return SimplePublicObjectInputForCreate(properties=self.dict())


class HubspotCompany(HubspotModel):
    name: str
    domain: str
    city: str | None = None
    industry: str | None = None
    phone: str | None = None
    state: str | None = None


class HubspotContact(HubspotModel):
    firstname: str
    lastname: str
    email: str
    initial_message: str | None = None
    phone: str | None = None
    company: str | None = None


class HubspotAPIReponse(BaseModel):
    id: str
    properties: dict[str, str]
    created_at: datetime
    updated_at: datetime
    archived: bool
