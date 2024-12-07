from sqlalchemy import insert, select
from typing import Sequence

from db.models import Relationship
from db.repository.base import BaseDatabaseRepository
from schemas.relationship import CreateRelationshipSchema


class RelationshipRepository(BaseDatabaseRepository):
    async def create_relationship(self, relationship: CreateRelationshipSchema) -> None:
        query = insert(Relationship).values(**relationship.model_dump())

        await self._session.execute(query)
        await self._session.commit()

    async def get_relationships_by_person_id(self, relative_id: int, existing_id: int) -> Sequence[Relationship]:
        query = select(Relationship).where(
            Relationship.relative_id == relative_id, Relationship.person_id != existing_id
        )

        results = await self._session.execute(query)
        return results.scalars().all()
