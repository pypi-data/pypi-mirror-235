import typing as t
import json
from algoliasearch.search_client import SearchClient

from .client_factory import AlgoliaClientFactory
from .models import AlgoliaIndex, AlgoliaSearchParams, AlgoliaSearchResults


class AlgoliaSearchRepository:
    def __init__(
        self,
        index_name: AlgoliaIndex,
        client: SearchClient | None = None,
    ):
        self.client = client or AlgoliaClientFactory.get_client()
        self.index = self.client.init_index(index_name.value)

    def search(self, query: AlgoliaSearchParams):
        query_text = query.query
        return AlgoliaSearchResults(**self.index.search(query_text))

    def get_object(self, object_id: str):
        return self.index.get_object(object_id)

    def create_object(self, object_id: str, object_data: dict):
        object_data["objectID"] = object_id
        object_data = json.loads(json.dumps(object_data, default=str))
        return self.index.save_object(object_data)

    def update_object(self, object_id: str, object_data: dict):
        object_data["objectID"] = object_id
        object_data = json.loads(json.dumps(object_data, default=str))
        return self.index.partial_update_object(object_data)

    def get_all_objects_with_attribute(
        self, attribute_name: str, attribute_value: t.Any
    ):
        objects = self.index.search(query=f"{attribute_name}={attribute_value}")
        return [object_dict["objectID"] for object_dict in objects["hits"]]

    def partial_update_based_on_attribute(self, objects_to_update: list[dict]):
        """
        Provide a list of dictionaries of partials updates for objects.
        These objects must have an attribute that matches the filter_attribute.
        The filter attribute will be used to filter objects in the database and then
        the partial update will be applied to the filtered objects.
        """
        return self.index.partial_update_objects(objects_to_update)  # type: ignore

    def delete_object(self, object_id: str):
        return self.index.delete_object(object_id)
