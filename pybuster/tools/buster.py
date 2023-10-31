import aiohttp
import asyncio
from .custom_types import UrlInfo
from .exceptions import BadConnectionError
from typing import List


class Buster:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def get_code(self, url) -> UrlInfo:
        try:
            async with self.session.get(url) as response:
                return UrlInfo(url, response.status)
        except Exception:
            raise BadConnectionError

    async def get_codes(self, base_url: str, endpoints: List[str]) -> List[UrlInfo]:
        tasks = []
        for endpoint in endpoints:
            url = (
                base_url + endpoint
                if base_url.endswith("/")
                else base_url + "/" + endpoint
            )
            tasks.append(self.get_code(url))
        urls_and_codes = await asyncio.gather(*tasks)
        return urls_and_codes
