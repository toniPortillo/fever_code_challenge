from src.domain.end_date import EndDate
from src.domain.end_time import EndTime
from src.domain.event import Event
from src.domain.event_id import EventId
from src.domain.start_date import StartDate
from src.domain.start_time import StartTime
from src.domain.max_price import MaxPrice
from src.domain.min_price import MinPrice
from src.domain.title import Title
from src.shared.domain.domain_exceptions import (
    DomainException,
)


class EventFactoryMethod:
    @classmethod
    async def build_event(
        cls,
        event_id: str,
        title: str,
        start_date: str,
        start_time: str,
        end_date: str,
        end_time: str,
        min_price: float,
        max_price: float,
    ) -> Event:
        try:
            event_id_vo: EventId = EventId(
                event_id,
            )
            title_vo: Title = Title(
                title,
            )
            start_date_vo: StartDate = StartDate(
                start_date,
            )
            start_time_vo: StartTime = StartTime(
                start_time,
            )
            end_date_vo: EndDate = EndDate(
                end_date,
            )
            end_time_vo: EndTime = EndTime(
                end_time,
            )
            min_price_vo: MinPrice = MinPrice(
                min_price,
            )
            max_price_vo: MaxPrice = MaxPrice(
                max_price,
            )

            event: Event = Event(
                event_id_vo,
                title_vo,
                start_date_vo,
                start_time_vo,
                end_date_vo,
                end_time_vo,
                min_price_vo,
                max_price_vo,
            )
            return event
        except DomainException as domain_exception:
            raise DomainException(
                domain_exception.domain_artifact,
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
