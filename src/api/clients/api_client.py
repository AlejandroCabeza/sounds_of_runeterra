# Python Imports
# Third-Party Imports
# Project Imports
from src.api.clients.http_client import HttpClient
from src.api.clients.api_config import (
    ENDPOINT_STATIC_DECKLIST,
    ENDPOINT_POSITIONAL_RECTANGLES,
    ENDPOINT_GAME_RESULT,
    ENDPOINT_EXPEDITIONS_STATE
)


class ApiClient:

    def __init__(self, http_client: HttpClient = HttpClient()):
        self._http_client: HttpClient = http_client

    async def fetch_static_decklist(self):
        return await self._http_client.fetch_as_json(ENDPOINT_STATIC_DECKLIST)

    async def fetch_positional_rectangles(self):
        return await self._http_client.fetch_as_json(ENDPOINT_POSITIONAL_RECTANGLES)

    async def fetch_expeditions_state(self):
        return await self._http_client.fetch_as_json(ENDPOINT_GAME_RESULT)

    async def fetch_game_result(self):
        return await self._http_client.fetch_as_json(ENDPOINT_EXPEDITIONS_STATE)
