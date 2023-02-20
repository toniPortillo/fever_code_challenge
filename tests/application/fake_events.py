from typing import List, Dict, Any

from src.domain.event import Event
from src.domain.event_factory_method import (
    EventFactoryMethod,
)


fake_events: List[Dict[str, Any]] = [
    {
        "id": "291",
        "title": "Camela en concierto",
        "start_date": "2021-06-30",
        "start_time": "21:00:00",
        "end_date": "2021-06-30",
        "end_time": "22:00:00",
        "min_price": 15.0,
        "max_price": 30.0,
    },
    {
        "id": "322",
        "title": "Pantomima Full",
        "start_date": "2021-02-10",
        "start_time": "20:00:00",
        "end_date": "2021-02-10",
        "end_time": "21:30:00",
        "min_price": 30.0,
        "max_price": 55.0,
    },
    {
        "id": "1591",
        "title": "Los Morancos",
        "start_date": "2021-07-31",
        "start_time": "20:00:00",
        "end_date": "2021-07-31",
        "end_time": "21:00:00",
        "min_price": 65.0,
        "max_price": 75.0,
    },
]


async def build_fake_event_list() -> List[Event]:
    events: List[Event] = [
        await EventFactoryMethod.build_event(
            event["id"],
            event["title"],
            event["start_date"],
            event["start_time"],
            event["end_date"],
            event["end_time"],
            event["min_price"],
            event["max_price"],
        )
        for event in fake_events
    ]

    return events
