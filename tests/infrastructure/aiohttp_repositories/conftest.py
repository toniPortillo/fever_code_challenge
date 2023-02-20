# import pytest
from typing import Optional, Any
from unittest.mock import AsyncMock


class AsyncContextManager:
    def __init__(self, async_mock: Optional[AsyncMock] = None) -> None:
        self.__async_mock = async_mock

    async def __aenter__(self) -> Optional[AsyncMock]:
        return self.__async_mock

    async def __aexit__(self, exc_type: str, exc: str, tb: str) -> Any:
        pass
