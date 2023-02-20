from fastapi.responses import JSONResponse
from typing import Any, Dict, Union
from pydantic import BaseModel


class APIResponse(BaseModel):
    openapi_info: Dict[Union[int, str], Dict[str, Any]]
    response: JSONResponse

    class Config:
        arbitrary_types_allowed = True
