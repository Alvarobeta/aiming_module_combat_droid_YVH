from fastapi import APIRouter

from app.target_selector.infrastructure.FastAPI.api_v1.endpoints import radar

api_router = APIRouter()
api_router.include_router(radar.router, tags=["radar"])
