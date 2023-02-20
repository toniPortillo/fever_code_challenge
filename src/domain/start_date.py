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
class StartDate:
    start_date: str

    @validator("start_date")
    def start_date_validator(cls, start_date: str) -> str:
        try:
            pattern: str = r"^[2-9]{1}[0-9]{3}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}$"
            if not re.match(pattern, start_date):
                raise DomainException(
                    "StartDate", INVALID_FIELD, "Invalid star date pattern"
                )
            time.strptime(start_date, "%Y-%m-%d")
            return start_date
        except DomainException as domain_exception:
            raise DomainException(
                domain_exception.domain_artifact,
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
        except Exception:
            raise DomainException(
                "StartDate", INVALID_FIELD, "Invalid star date pattern"
            )
