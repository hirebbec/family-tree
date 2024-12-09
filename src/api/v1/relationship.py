from fastapi import APIRouter, status, Depends

from schemas.person import GetPersonWithRelationshipTreeSchema
from schemas.relationship import CreateRelationshipSchema, UpdateRelationshipSchema
from services.relationship import RelationshipService

router = APIRouter(prefix="/relationship", tags=["Relationships"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_relationship(
    relationship: CreateRelationshipSchema,
    relationship_service: RelationshipService = Depends(),
) -> None:
    await relationship_service.create_relationship(relationship=relationship)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=GetPersonWithRelationshipTreeSchema)
async def get_relationship_tree_by_id(
    id: int,
    relationship_service: RelationshipService = Depends(),
) -> GetPersonWithRelationshipTreeSchema:
    return await relationship_service.get_relationship_tree_by_id(id=id, existing_id=id)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=None)
async def update_relationship(
    id: int,
    relationship: UpdateRelationshipSchema,
    relationship_service: RelationshipService = Depends(),
) -> None:
    await relationship_service.update_relationship_by_id(id=id, relationship=relationship)


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=None)
async def delete_relationship_id(
    id: int,
    relationship_service: RelationshipService = Depends(),
) -> None:
    return await relationship_service.delete_relationship_by_id(id=id)
