from typing import List, Tuple

from src.application.event_response_dto import (
    EventResponseDto,
)
from src.domain.event import (
    Event,
)
from src.domain.event_repository import (
    EventRepository,
)
from src.domain.end_date import EndDate
from src.domain.end_time import EndTime
from src.domain.format_dates_service import (
    FormatDatesService,
)
from src.domain.previous_event_repository import (
    PreviousEventRepository,
)
from src.domain.select_events_by_date_service import (
    SelectEventsByDateService,
)
from src.domain.start_date import StartDate
from src.domain.start_time import StartTime
from src.shared.application.application_exception import (
    ApplicationException,
)
from src.shared.domain.domain_exceptions import DomainException


class GetEventListUseCase:
    def __init__(
        self,
        event_repository: EventRepository,
        previous_event_repository: PreviousEventRepository,
    ) -> None:
        self.__event_repository = event_repository
        self.__previous_event_repository = previous_event_repository

    async def get_event_list(
        self,
        start_at: str,
        ends_at: str,
    ) -> List[EventResponseDto]:
        try:
            dates: Tuple[
                StartDate, StartTime, EndDate, EndTime
            ] = await FormatDatesService.format_dates(
                start_at,
                ends_at,
            )
            events: List[
                Event
            ] = await self.__event_repository.get_events_from_provider()

            updated_events: List[
                Event
            ] = await self.__previous_event_repository.update_events(events)

            selected_events: List[
                Event
            ] = await SelectEventsByDateService.select_events(
                updated_events,
                dates[0],
                dates[2],
            )
            event_reponse_dto: List[EventResponseDto] = [
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
                for event in selected_events
            ]

            return event_reponse_dto
        except DomainException as domain_exception:
            raise ApplicationException(
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
        except ApplicationException as application_exception:
            raise ApplicationException(
                application_exception.standard_exception,
                application_exception.exception_message,
            )
