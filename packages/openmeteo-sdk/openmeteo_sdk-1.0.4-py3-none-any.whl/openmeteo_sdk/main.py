"""This is a Sample Python file."""


from __future__ import annotations

import asyncio
from typing import AsyncGenerator

# import aiohttp
# import pandas as pd
from aiohttp_client_cache import CachedSession, SQLiteBackend

# from aiohttp_client_cache.session import CacheMixin
from aiohttp_retry import ExponentialRetry, RetryClient

from openmeteo_sdk.fb.AirQualityApiResponse import AirQualityApiResponse
from openmeteo_sdk.fb.ClimateApiResponse import ClimateApiResponse
from openmeteo_sdk.fb.EnsembleApiResponse import EnsembleApiResponse
from openmeteo_sdk.fb.FloodApiResponse import FloodApiResponse
from openmeteo_sdk.fb.MarineApiResponse import MarineApiResponse
from openmeteo_sdk.fb.SiUnit import SiUnit
from openmeteo_sdk.fb.WeatherApiResponse import WeatherApiResponse

# class CustomSession(CacheMixin, RetryClient, aiohttp.ClientSession):
#    """Session with features from both aiohttp_client_cache and some_other_library"""


def unit_to_name(code):
    """convert SiUnit to name"""
    for name, value in SiUnit.__dict__.items():
        if value == code:
            return name
    return None


async def _decode_stream(stream: asyncio.StreamReader):
    """Decode stream assuming first 4 bytes are message length"""
    while ~stream.at_eof():
        try:
            length = int.from_bytes(await stream.readexactly(4), "little")
        except asyncio.exceptions.IncompleteReadError:
            break
        yield await stream.readexactly(length)


async def decode_weather_api_response(stream: asyncio.StreamReader) -> AsyncGenerator[WeatherApiResponse, None]:
    """Decode stream as sequence of weather api responses"""
    async for message in _decode_stream(stream):
        yield WeatherApiResponse.GetRootAs(message, 0)


async def decode_air_quality_api_response(
    stream: asyncio.StreamReader,
) -> AsyncGenerator[AirQualityApiResponse, None, None]:
    """Decode stream as sequence of air quality api responses"""
    async for message in _decode_stream(stream):
        yield AirQualityApiResponse.GetRootAs(message, 0)


async def decode_flood_api_response(stream: asyncio.StreamReader) -> AsyncGenerator[FloodApiResponse, None]:
    """Decode stream as sequence of flood api responses"""
    async for message in _decode_stream(stream):
        yield FloodApiResponse.GetRootAs(message, 0)


async def decode_marine_api_response(stream: asyncio.StreamReader) -> AsyncGenerator[MarineApiResponse, None]:
    """Decode stream as sequence of marine api responses"""
    async for message in _decode_stream(stream):
        yield MarineApiResponse.GetRootAs(message, 0)


async def decode_climate_api_response(stream: asyncio.StreamReader) -> AsyncGenerator[ClimateApiResponse, None]:
    """Decode stream as sequence of climate api responses"""
    async for message in _decode_stream(stream):
        yield ClimateApiResponse.GetRootAs(message, 0)


async def decode_ensemble_api_response(stream: asyncio.StreamReader) -> AsyncGenerator[EnsembleApiResponse, None]:
    """Decode stream as sequence of ensemble api responses"""
    async for message in _decode_stream(stream):
        yield EnsembleApiResponse.GetRootAs(message, 0)


# default_cache = SQLiteBackend(".cache.sqlite")


# = SQLiteBackend("demo_cache")


async def fetch_dummy_old():
    """test"""
    retry_options = ExponentialRetry(attempts=10)
    async with CachedSession(cache=SQLiteBackend("demo_cache"), expire_after=-1) as session:
        retry_client = RetryClient(client_session=session, raise_for_status=False, retry_options=retry_options)
        params = {
            "latitude": [52.54],  # , 48.1, 48.4],
            "longitude": [13.41],  # , 9.31, 8.5],
            "hourly": ["temperature_2m", "precipitation"],
            "start_date": "2022-01-01",
            "end_date": "2023-08-01",
            # 'timezone': 'auto',
            # 'current': ['temperature_2m','precipitation'],
            # 'current_weather': 1,
            "format": "flatbuffers",
        }
        async with retry_client.get(
            "https://archive-api.open-meteo.com/v1/archive", params=params, compress=True
        ) as response:
            if response.status != 200:
                print(response.status)
                return

            async for res in decode_weather_api_response(response.content):
                print("Coordinates ", res.Latitude(), res.Longitude(), res.Elevation())
                print(res.Timezone(), res.TimezoneAbbreviation())
                print("Generation time", res.GenerationtimeMs())

                # hourly = res.Hourly()
                # date = pd.date_range(
                #     start=pd.to_datetime(hourly.Time().Start(), unit="s"),
                #     end=pd.to_datetime(hourly.Time().End(), unit="s"),
                #     freq=pd.Timedelta(seconds=hourly.Time().Interval()),
                #     inclusive="left",
                # )

                # print(date)

                # df = pd.DataFrame(
                #     data={
                #         "date": date,
                #         "temperature_2m": hourly.Temperature2m().ValuesAsNumpy(),
                #         "precipitation": hourly.Precipitation().ValuesAsNumpy(),
                #     }
                # )

                # print(df)

                # print("Current temperature", res.Current().Temperature2m().Value())
                # print("Current Precipitation", res.Current().Precipitation().Value())
                # print()

                # print(df.groupby(df.date.dt.day)["temperature_2m"].agg(["sum", "mean", "max"]))
            response.closed = True


def hello_world(i: int = 0) -> str:
    """Doc String."""
    print("hello world")
    return f"string-{i}"


def good_night() -> str:
    """Doc String."""
    print("good night")
    return "string"


def hello_goodbye():
    """a"""
    hello_world(1)
    good_night()
