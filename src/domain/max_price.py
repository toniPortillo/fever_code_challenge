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
class MaxPrice:
    max_price: float

    @validator("max_price")
    def max_price_validator(cls, max_price: float) -> float:
        try:
            pattern: str = r"^[0-9]{1,}.{0,1}[0-9]{0,}$"
            if not re.match(pattern, str(max_price)):
                raise DomainException(
                    "MaxPrice",
                    INVALID_FIELD,
                    "Invalid max price pattern",
                )
            return max_price
        except DomainException as domain_exception:
            raise DomainException(
                domain_exception.domain_artifact,
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
