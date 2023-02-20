from typing import Dict, List, Optional, Any
from pydantic import BaseModel

from src.application.event_response_dto import (
    EventResponseDto,
)


class GetEventListResponseSchema(BaseModel):
    data: Dict[str, List[EventResponseDto]]
    error: Optional[str]

    class Config:
        schema_extra: Dict[str, Any] = {
            "example": {
                "data": {
                    "events": [
                        {
                            "id": "101",
                            "title": "Charlotte de Witte",
                            "start_date": "2021-07-04",
                            "start_time": "21:00:00",
                            "end_date": "2021-07-04",
                            "end_time": "24:00:00",
                            "min_price": 15.5,
                            "max_price": 30.5,
                        },
                        {
                            "id": "251",
                            "title": "Amelie Lens",
                            "start_date": "2021-08-14",
                            "start_time": "21:00:00",
                            "end_date": "2021-08-14",
                            "end_time": "24:00:00",
                            "min_price": 25.5,
                            "max_price": 50.5,
                        },
                    ]
                },
                "error": "None",
            }
        }
