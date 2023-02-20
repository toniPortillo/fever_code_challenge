from typing import Final

from fastapi.responses import JSONResponse

from src.shared.dtos.api_response import APIResponse


NOT_FOUND: Final[APIResponse] = APIResponse(
    openapi_info={404: {"model": None}}, response=JSONResponse(status_code=404)
)

INVALID_FIELD_STATUS_CODE: Final[int] = 403

NOT_FOUND_STATUS_CODE: Final[int] = 404

DEPENDENCY_PROBLEM_STATUS_CODE: Final[int] = 422

CONFLICT_STATUS_CODE: Final[int] = 409

NOT_ACCEPTABLE_STATUS_CODE: Final[int] = 406
