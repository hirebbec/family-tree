from typing import Sequence

from sqlalchemy import insert, select

from db.models import Person
from db.repository.base import BaseDatabaseRepository
from schemas.person import CreatePersonSchema


class PersonRepository(BaseDatabaseRepository):
    async def create_person(self, person: CreatePersonSchema) -> None:
        query = insert(Person).values(**person.model_dump())

        await self._session.execute(query)
        await self._session.commit()

    async def get_person_by_id(self, id: int) -> Person | None:
        query = select(Person).where(Person.id == id)

        result = await self._session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> Sequence[Person]:
        query = select(Person)

        result = await self._session.execute(query)
        return result.scalars().all()
