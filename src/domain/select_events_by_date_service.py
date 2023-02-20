import time
from typing import List, Any

from src.domain.event import Event
from src.domain.start_date import StartDate
from src.domain.end_date import EndDate


class SelectEventsByDateService:
    @classmethod
    async def select_events(
        cls,
        event_list: List[Event],
        start_at: StartDate,
        ends_at: EndDate,
    ) -> List[Event]:
        start_date: Any = time.strptime(start_at.start_date, "%Y-%m-%d")
        end_date: Any = time.strptime(ends_at.end_date, "%Y-%m-%d")

        seleted_events: List[Event] = [
            event
            for event in event_list
            if (
                time.strptime(event.start_date, "%Y-%m-%d") >= start_date
                and time.strptime(event.end_date, "%Y-%m-%d") <= end_date
            )
        ]
        return seleted_events
