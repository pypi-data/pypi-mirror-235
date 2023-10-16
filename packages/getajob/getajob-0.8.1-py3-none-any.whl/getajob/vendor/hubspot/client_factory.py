from hubspot import HubSpot

from getajob.config.settings import SETTINGS
from getajob.abstractions.vendor_client_factory import VendorClientFactory

from .mock import MockHubspot


class HubspotClientFactory(VendorClientFactory):
    @staticmethod
    def _return_mock():
        return MockHubspot()

    @staticmethod
    def _return_client():
        return HubSpot(access_token=SETTINGS.HUBSPOT_TOKEN)
