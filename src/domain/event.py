from pydantic.dataclasses import dataclass

from src.domain.end_date import EndDate
from src.domain.end_time import EndTime
from src.domain.event_id import EventId
from src.domain.start_date import StartDate
from src.domain.start_time import StartTime
from src.domain.max_price import MaxPrice
from src.domain.min_price import MinPrice
from src.domain.title import Title


@dataclass
class Event:
    def __init__(
        self,
        event_id: EventId,
        title: Title,
        start_date: StartDate,
        start_time: StartTime,
        end_date: EndDate,
        end_time: EndTime,
        min_price: MinPrice,
        max_price: MaxPrice,
    ) -> None:
        self.__event_id = event_id
        self.__title = title
        self.__start_date = start_date
        self.__start_time = start_time
        self.__end_date = end_date
        self.__end_time = end_time
        self.__min_price = min_price
        self.__max_price = max_price

    @property
    def event_id(self) -> str:
        return self.__event_id.event_id

    @property
    def title(self) -> str:
        return self.__title.title

    @property
    def start_date(self) -> str:
        return self.__start_date.start_date

    @property
    def start_time(self) -> str:
        return self.__start_time.start_time

    @property
    def end_date(self) -> str:
        return self.__end_date.end_date

    @property
    def end_time(self) -> str:
        return self.__end_time.end_time

    @property
    def min_price(self) -> float:
        return self.__min_price.min_price

    @property
    def max_price(self) -> float:
        return self.__max_price.max_price
