from fastapi import APIRouter

from core.config import settings
from api.v1.person import router as person_router
from api.v1.relationship import router as relationship_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(person_router)
v1_router.include_router(relationship_router)


project_router = APIRouter(prefix=f"{settings().PROJECT_NAME}")
project_router.include_router(v1_router)
