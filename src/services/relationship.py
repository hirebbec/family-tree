from fastapi import Depends

from core.exceptions import person_not_found_exception, relationship_conflict_exception
from db.repository.person import PersonRepository
from db.repository.relationship import RelationshipRepository
from schemas.relationship import CreateRelationshipSchema
from services.base import BaseService


class RelationshipService(BaseService):
    def __init__(self, relationship_repository: RelationshipRepository = Depends(), person_repository: PersonRepository = Depends()):
        self._relationship_repository = relationship_repository
        self._person_repository = person_repository

    async def create_relationship(self, relationship: CreateRelationshipSchema) -> None:
        if relationship.person_id == relationship.relative_id:
            raise relationship_conflict_exception

        if not await self._person_repository.get_person_by_id(id=relationship.person_id):
            raise person_not_found_exception

        if not await self._person_repository.get_person_by_id(id=relationship.relative_id):
            raise person_not_found_exception

        await self._relationship_repository.create_relationship(
            relationship=relationship
        )
