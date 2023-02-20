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
class Title:
    title: str

    @validator("title")
    def title_validator(cls, title: str) -> str:
        try:
            pattern: str = r"^[A-Za-z0-9 ]{3,}$"
            if not re.match(pattern, title):
                raise DomainException(
                    "Title",
                    INVALID_FIELD,
                    "Invalid title pattern",
                )
            return title
        except DomainException as domain_exception:
            raise DomainException(
                domain_exception.domain_artifact,
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
