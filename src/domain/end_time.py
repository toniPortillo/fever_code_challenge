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
class EndTime:
    end_time: str

    @validator("end_time")
    def end_time_validator(cls, end_time: str) -> str:
        try:
            pattern: str = r"^[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1}$"
            if not re.match(pattern, end_time):
                raise DomainException(
                    "EndTime", INVALID_FIELD, "Invalid end time pattern"
                )
            time.strptime(end_time, "%H:%M:%S")
            return end_time
        except DomainException as domain_exception:
            raise DomainException(
                domain_exception.domain_artifact,
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
        except Exception:
            raise DomainException("EndTime", INVALID_FIELD, "Invalid end time pattern")
