import pytest
from typing import List

from src.application.get_event_list_use_case import (
    GetEventListUseCase,
)
from src.application.event_response_dto import (
    EventResponseDto,
)
from tests.application.mock_event_repository import (
    MockEventRepository,
)
from tests.application.mock_previous_event_repository import (
    MockPreviousEventRepository,
)
from tests.application.tests_get_event_list_use_case.fake_get_event_list_response_dto import (
    build_fake_event_list_response_dto,
)


class TestGetEventListUseCase:
    @pytest.mark.asyncio
    async def test_get_event_list_success(
        self,
    ) -> None:
        mock_event_repository: MockEventRepository = MockEventRepository()
        mock_previous_event_repository: MockPreviousEventRepository = (
            MockPreviousEventRepository()
        )
        get_event_list_use_case: GetEventListUseCase = GetEventListUseCase(
            mock_event_repository, mock_previous_event_repository
        )
        fake_event_list_respose_dto: List[
            EventResponseDto
        ] = await build_fake_event_list_response_dto()

        start_at: str = "2021-02-01T17:32:28Z"
        ends_at: str = "2022-07-03T17:32:28Z"
        event_list_response_dto: List[
            EventResponseDto
        ] = await get_event_list_use_case.get_event_list(start_at, ends_at)

        assert event_list_response_dto == fake_event_list_respose_dto
