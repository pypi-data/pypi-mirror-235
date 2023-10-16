from hubspot.client import Client as HubspotClient
from hubspot.crm.contacts.exceptions import ApiException

from getajob.exceptions import HubspotAPIException

from .models import HubspotCompany, HubspotContact
from .client_factory import HubspotClientFactory


class HubspotRepository:
    def __init__(self, client: HubspotClient | None = None):
        self.client = client or HubspotClientFactory.get_client()

    def create_contact(self, contact: HubspotContact):
        try:
            resp = self.client.crm.contacts.basic_api.create(
                simple_public_object_input_for_create=contact.to_hubspot()
            )
            return resp.__dict__["_properties"]
        except ApiException as exc:
            raise HubspotAPIException(str(exc.reason))

    def create_company(self, company: HubspotCompany):
        try:
            resp = self.client.crm.companies.basic_api.create(
                simple_public_object_input_for_create=company.to_hubspot()
            )
            return resp.__dict__["_properties"]
        except ApiException as exc:
            raise HubspotAPIException(str(exc.reason))
