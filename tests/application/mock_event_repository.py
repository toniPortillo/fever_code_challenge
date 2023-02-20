from typing import List

from src.domain.event import Event
from src.domain.event_repository import EventRepository
from tests.application.fake_events import (
    build_fake_event_list,
)


class MockEventRepository(EventRepository):
    async def get_events_from_provider(self) -> List[Event]:
        return await build_fake_event_list()
