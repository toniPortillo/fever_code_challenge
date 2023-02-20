from typing import Tuple, List

from src.domain.start_date import StartDate
from src.domain.start_time import StartTime
from src.domain.end_date import EndDate
from src.domain.end_time import EndTime

from src.shared.application.application_exception import (
    ApplicationException,
)
from src.shared.domain.domain_exceptions import DomainException


class FormatDatesService:
    @classmethod
    async def format_dates(
        cls,
        start_at: str,
        ends_at: str,
    ) -> Tuple[StartDate, StartTime, EndDate, EndTime]:
        try:
            start_date: List[str] = start_at.split("T")
            ends_date: List[str] = ends_at.split("T")
            start_date_vo: StartDate = StartDate(
                start_date[0],
            )
            end_date_vo: EndDate = EndDate(
                ends_date[0],
            )
            start_time: List[str] = start_date[1].split("Z")
            end_time: List[str] = ends_date[1].split("Z")
            start_time_vo: StartTime = StartTime(
                start_time[0],
            )
            end_time_vo: EndTime = EndTime(
                end_time[0],
            )

            return start_date_vo, start_time_vo, end_date_vo, end_time_vo
        except DomainException as domain_exception:
            raise ApplicationException(
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
