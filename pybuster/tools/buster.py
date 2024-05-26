import asyncio
import httpx

from .custom_types import UrlInfo
from .exceptions import BadConnectionError


class Buster:
    def __init__(self):
        self.session = httpx.AsyncClient()

    async def get_code(self, url: str) -> UrlInfo:
        # try:
        response = await self.session.get(url)
        if response.status_code != 301:
            print(response, url)
        return UrlInfo(url=url, code=response.status_code)
        # except Exception:
        #     raise BadConnectionError

    async def get_codes(self, base_url: str, endpoints: list[str]) -> list[UrlInfo]:
        tasks = [self.get_code(base_url + endpoint if base_url.endswith("/") else base_url + "/" + endpoint) for endpoint in endpoints]
        urls_and_codes = await asyncio.gather(*tasks)
        return urls_and_codes