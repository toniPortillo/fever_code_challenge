import datetime
from typing import Union, Optional
import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse
import xmltodict

from src.application.get_event_list_use_case import (
    GetEventListUseCase,
)
from src.infrastructure.api.api_v1.json_exception_responses.json_response_builder import (
    JsonResponseBuilder,
)
from src.infrastructure.aiohttp_repositories.event_aiohttp_repository import (
    EventAiohttpRepository,
)
from src.infrastructure.json_file_repositories.previous_event_json_file_repository import (
    PreviousEventJsonFileRepository,
)
from src.infrastructure.api.api_v1.models.get_event_list_response_schema import (
    GetEventListResponseSchema,
)
from src.infrastructure.api.api_v1.models.error_response import (
    ErrorResponse,
)
from src.shared.application.application_exception import (
    ApplicationException,
)
from src.shared.config.singleton_aiohttp import (
    SingletonAiohttp,
)

router: APIRouter = APIRouter()


@router.get(
    "",
    description="Get events between two dates",
    status_code=200,
    response_model=GetEventListResponseSchema,
    summary="Get event list between two dates",
    responses={
        422: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
        406: {"model": ErrorResponse},
    },
)
async def get_event_list(
    start_at: str = "2021-02-01T17:32:28Z",
    ends_at: str = "2022-07-03T17:32:28Z",
) -> Union[GetEventListResponseSchema, Optional[JSONResponse]]:
    try:
        start_time = datetime.datetime.now()

        event_aiohttp_repository: EventAiohttpRepository = EventAiohttpRepository(
            SingletonAiohttp.get_aiohttp_client(),
            xmltodict.parse,
        )
        previous_event_json_repository: PreviousEventJsonFileRepository = (
            PreviousEventJsonFileRepository(
                json.dump,
                json.load,
            )
        )

        get_event_list_use_case: GetEventListUseCase = GetEventListUseCase(
            event_aiohttp_repository,
            previous_event_json_repository,
        )

        time_diff = datetime.datetime.now() - start_time
        execution_time = time_diff.total_seconds() * 1000
        print(f"{execution_time}ms")

        return GetEventListResponseSchema(
            data={
                "events": await get_event_list_use_case.get_event_list(
                    start_at,
                    ends_at,
                )
            }
        )
    except ApplicationException as application_exception:
        json_response: Optional[
            JSONResponse
        ] = await JsonResponseBuilder.build_json_response(
            application_exception.standard_exception,
            application_exception.exception_message,
        )
        return json_response
