from fastapi import APIRouter

from core.config import settings


v1_router = APIRouter(prefix="/v1")


project_router = APIRouter(prefix=f"{settings().PROJECT_NAME}")
project_router.include_router(v1_router)
