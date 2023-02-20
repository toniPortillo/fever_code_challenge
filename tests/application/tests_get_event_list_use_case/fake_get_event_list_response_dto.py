from typing import List

from src.application.event_response_dto import (
    EventResponseDto,
)
from src.domain.event import Event
from tests.application.fake_events import (
    build_fake_event_list,
)


async def build_fake_event_list_response_dto() -> List[EventResponseDto]:
    event_list: List[Event] = await build_fake_event_list()
    get_event_list_reponse_dto: List[EventResponseDto] = [
        EventResponseDto(
            id=event.event_id,
            title=event.title,
            start_date=event.start_date,
            start_time=event.start_time,
            end_date=event.end_date,
            end_time=event.end_time,
            min_price=event.min_price,
            max_price=event.max_price,
        )
        for event in event_list
    ]

    return get_event_list_reponse_dto
