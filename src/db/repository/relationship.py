from sqlalchemy import insert, select, update, delete
from typing import Sequence

from db.models import Relationship
from db.repository.base import BaseDatabaseRepository
from schemas.relationship import CreateRelationshipSchema, UpdateRelationshipSchema


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

    async def get_relationship_by_id(self, id: int) -> Relationship | None:
        query = select(Relationship).where(Relationship.id == id)

        results = await self._session.execute(query)
        return results.scalars().first()

    async def update_relationship_by_id(self, id: int, relationship: UpdateRelationshipSchema) -> None:
        query = update(Relationship).where(Relationship.id == id).values(**relationship.model_dump())

        await self._session.execute(query)
        await self._session.commit()

    async def update_relationship(self, relationship: CreateRelationshipSchema) -> None:
        query = (
            update(Relationship)
            .where(
                Relationship.person_id == relationship.person_id, Relationship.relative_id == relationship.relative_id
            )
            .values(**relationship.model_dump())
        )

        await self._session.execute(query)
        await self._session.commit()

    async def delete_relationship_by_id(self, id: int) -> None:
        query = delete(Relationship).where(Relationship.id == id)

        await self._session.execute(query)
        await self._session.commit()

    async def delete_relationships_by_person_id(self, person_id: int) -> None:
        query = delete(Relationship).where(Relationship.person_id == person_id)

        await self._session.execute(query)
        await self._session.commit()

    async def delete_relationships_by_relative_id(self, relative_id: int) -> None:
        query = delete(Relationship).where(Relationship.relative_id == relative_id)

        await self._session.execute(query)
        await self._session.commit()

    async def delete_relationship_by_person_id_and_relative_id(self, person_id: int, relative_id: int) -> None:
        query = delete(Relationship).where(Relationship.person_id == person_id, Relationship.relative_id == relative_id)

        await self._session.execute(query)
        await self._session.commit()
