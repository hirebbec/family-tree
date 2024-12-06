from fastapi import APIRouter, status, Depends

from schemas.relationship import CreateRelationshipSchema
from services.relationship import RelationshipService

router = APIRouter(prefix="/relationship", tags=["Relationships"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_relationship(
    relationship: CreateRelationshipSchema,
    relationship_service: RelationshipService = Depends(),
) -> None:
    await relationship_service.create_relationship(relationship=relationship)
