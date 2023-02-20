from src.infrastructure.api.responses import NOT_FOUND
from src.domain.exceptions import NotFoundException
from typing import Optional, Union
from fastapi.responses import JSONResponse
from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    summary="Show a Hello world!",
    status_code=200,
    responses={**NOT_FOUND.openapi_info},
)
async def hello_world_endpoint() -> Union[Optional[str], JSONResponse]:
    try:
        return "Hello world!"
    except NotFoundException:
        return NOT_FOUND.response
