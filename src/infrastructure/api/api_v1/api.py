from fastapi import APIRouter

# from src.infrastructure.api.api_v1.endpoints import hello_endpoints
from src.infrastructure.api.api_v1.endpoints import events

api_router = APIRouter()

# api_router.include_router(
#     hello_endpoints.router, prefix="/helloworlds", tags=["HelloWorld"]
# )
api_router.include_router(events.router, prefix="/events", tags=["Events"])
