from typing import List, Dict, Any

from src.domain.event import Event
from src.domain.previous_event_repository import (
    PreviousEventRepository,
)


class MockPreviousEventRepository(PreviousEventRepository):
    async def insert_events(
        self,
        events_list: List[Event],
    ) -> None:
        pass

    async def update_events(
        self,
        event_list: List[Event],
    ) -> List[Event]:
        return event_list

    async def read_events(
        self,
    ) -> Dict[str, Any]:
        pass
