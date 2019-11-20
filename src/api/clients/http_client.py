# Python Imports
import json
# Third-Party Imports
import aiohttp
# Project Imports
from src.api.clients.http_config import DEFAULT_IP, DEFAULT_PORT


class HttpClient:

    def __init__(self, ip: str = DEFAULT_IP, port: int = DEFAULT_PORT):
        self.url: str = f"http://{ip}:{port}"

    async def fetch(self, endpoint) -> str:
        async with aiohttp.ClientSession() as session:
            endpoint_url: str = f"{self.url}{endpoint}"
            async with session.get(endpoint_url) as response:
                return await response.text()

    async def fetch_as_json(self, endpoint) -> dict:
        return json.loads(await self.fetch(endpoint))
