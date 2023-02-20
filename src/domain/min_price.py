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
class MinPrice:
    min_price: float

    @validator("min_price")
    def min_price_validator(cls, min_price: float) -> float:
        try:
            pattern: str = r"^[0-9]{1,}.{0,1}[0-9]{0,}$"
            if not re.match(pattern, str(min_price)):
                raise DomainException(
                    "MinPrice",
                    INVALID_FIELD,
                    "Invalid min price pattern",
                )
            return min_price
        except DomainException as domain_exception:
            raise DomainException(
                domain_exception.domain_artifact,
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
