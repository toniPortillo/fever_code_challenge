from asgi_lifespan import LifespanManager
from typing import AsyncGenerator
from httpx import AsyncClient
import pytest

from src.main import app


@pytest.fixture()
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac
