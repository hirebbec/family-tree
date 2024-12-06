from sqlalchemy import insert

from db.models import Relationship
from db.repository.base import BaseDatabaseRepository
from schemas.relationship import CreateRelationshipSchema


class RelationshipRepository(BaseDatabaseRepository):
    async def create_relationship(self, relationship: CreateRelationshipSchema) -> None:
        query = insert(Relationship).values(**relationship.model_dump())

        await self._session.execute(query)
        await self._session.commit()
