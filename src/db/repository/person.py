from sqlalchemy import insert

from db.models import Person
from db.repository.base import BaseDatabaseRepository
from schemas.person import CreatePersonSchema


class PersonRepository(BaseDatabaseRepository):
    async def create_person(self, person: CreatePersonSchema) -> None:
        query = insert(Person).values(**person.model_dump())

        await self._session.execute(query)
        await self._session.commit()
