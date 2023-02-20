import re
import time

from pydantic import validator
from pydantic.dataclasses import dataclass

from src.shared.domain.exceptions import (
    INVALID_FIELD,
)
from src.shared.domain.domain_exceptions import (
    DomainException,
)


@dataclass(frozen=True)
class StartTime:
    start_time: str

    @validator("start_time")
    def start_time_validator(cls, start_time: str) -> str:
        try:
            pattern: str = r"^[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1}$"
            if not re.match(pattern, start_time):
                raise DomainException(
                    "StartTime", INVALID_FIELD, "Invalid start time pattern"
                )
            time.strptime(start_time, "%H:%M:%S")
            return start_time
        except DomainException as domain_exception:
            raise DomainException(
                domain_exception.domain_artifact,
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
        except Exception:
            raise DomainException(
                "StartTime", INVALID_FIELD, "Invalid start time pattern"
            )
