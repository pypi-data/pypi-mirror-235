"""Open Meteo API Client"""

from __future__ import annotations

from typing import AsyncGenerator

from aiohttp_client_cache import CacheBackend, CachedSession
from aiohttp_retry import ExponentialRetry, RetryClient

from openmeteo_sdk.fb.WeatherApiResponse import WeatherApiResponse

from .main import decode_weather_api_response


class Client:
    """Open Meteo API Client"""

    def __init__(self, expire_after: int = -1, cache: CacheBackend = None):
        retry_options = ExponentialRetry(attempts=10)
        self.session = CachedSession(cache=cache, expire_after=expire_after)
        self.client = RetryClient(client_session=self.session, raise_for_status=False, retry_options=retry_options)

    async def weather_api(self, url: str, params: any) -> AsyncGenerator[WeatherApiResponse, None]:
        """Fetch data and decode"""
        async with self.client.get(url, params=params, compress=True) as response:
            if response.status != 200:
                print(response.status)
                return
            async for result in decode_weather_api_response(response.content):
                yield result
            # if ~hasattr(response, "closed"):
            #     response.closed = False

    async def close(self):
        """close session"""
        await self.session.close()
