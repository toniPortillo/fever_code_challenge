import re

from pydantic import validator
from pydantic.dataclasses import dataclass

from src.shared.domain.exceptions import (
    INVALID_FIELD,
)
from src.shared.domain.domain_exceptions import (
    DomainException,
)


@dataclass(frozen=True)
class EventId:
    event_id: str

    @validator("event_id")
    def event_id_validator(cls, event_id: str) -> str:
        try:
            pattern: str = r"^[1-9][0-9]*$"
            if not re.match(pattern, event_id):
                raise DomainException(
                    "EventId",
                    INVALID_FIELD,
                    "Invalid event id pattern",
                )
            return event_id
        except DomainException as domain_exception:
            raise DomainException(
                domain_exception.domain_artifact,
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
