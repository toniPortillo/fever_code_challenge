import os
from typing import Any, Dict, Final, List

from fastapi import FastAPI

from src.infrastructure.api.api_v1.api import api_router
from src.shared.config.provider_configuration_constants import (
    PREVIOUS_EVENTS_JSON_FILE,
)
from src.shared.config.singleton_aiohttp import SingletonAiohttp


API_V: Final[str] = f"{os.getenv('SUB_PATH', '')}/api/v1"
tags_metadata: List[Dict[str, Any]] = [
    {
        "name": "Fever code challenge",
        "description": "We have an external provider that gives us some events from their company, and we want to integrate them on the Fever marketplace",
    }
]


async def on_start_up() -> None:
    SingletonAiohttp.get_aiohttp_client()
    if os.path.exists(PREVIOUS_EVENTS_JSON_FILE):
        os.remove(PREVIOUS_EVENTS_JSON_FILE)


async def on_shutdown() -> None:
    await SingletonAiohttp.close_aiohttp_client()


app = FastAPI(
    title="fever-code-challenge",
    openapi_url=f"{API_V}/openapi.json",
    openapi_tags=tags_metadata,
    on_startup=[on_start_up],
    on_shutdown=[on_shutdown],
)

app.include_router(api_router, prefix=API_V)
