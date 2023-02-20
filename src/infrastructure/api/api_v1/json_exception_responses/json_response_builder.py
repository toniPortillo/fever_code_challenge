from typing import Optional

from fastapi.responses import JSONResponse

from src.shared.domain.exceptions import (
    INVALID_FIELD,
    NOT_FOUND,
    DEPENDENCY_PROBLEM,
    CONFLICT,
    NOT_ACCEPTABLE,
)

from src.infrastructure.api.responses import (
    INVALID_FIELD_STATUS_CODE,
    NOT_FOUND_STATUS_CODE,
    DEPENDENCY_PROBLEM_STATUS_CODE,
    CONFLICT_STATUS_CODE,
    NOT_ACCEPTABLE_STATUS_CODE,
)


class JsonResponseBuilder:
    @classmethod
    async def build_json_response(
        cls,
        standard_exception: str,
        exception_message: str,
    ) -> Optional[JSONResponse]:
        if standard_exception == INVALID_FIELD:
            return JSONResponse(
                status_code=INVALID_FIELD_STATUS_CODE,
                content={"message": exception_message},
            )
        if standard_exception == NOT_FOUND:
            return JSONResponse(
                status_code=NOT_FOUND_STATUS_CODE,
                content={"message": exception_message},
            )
        if standard_exception == DEPENDENCY_PROBLEM:
            return JSONResponse(
                status_code=DEPENDENCY_PROBLEM_STATUS_CODE,
                content={"message": exception_message},
            )
        if standard_exception == CONFLICT:
            return JSONResponse(
                status_code=CONFLICT_STATUS_CODE, content={"message": exception_message}
            )
        if standard_exception == NOT_ACCEPTABLE:
            return JSONResponse(
                status_code=NOT_ACCEPTABLE_STATUS_CODE,
                content={"message": exception_message},
            )
        return None
