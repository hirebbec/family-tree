from typing import Sequence

from fastapi import Depends

from db.repository.person import PersonRepository
from schemas.person import CreatePersonSchema, GetPersonSchema
from services.base import BaseService


class PersonService(BaseService):
    def __init__(self, person_repository: PersonRepository = Depends()):
        self._person_repository = person_repository

    async def create_person(self, person: CreatePersonSchema) -> None:
        await self._person_repository.create_person(person=person)

    async def get_person_by_id(self, id: int) -> GetPersonSchema:
        person = await self._person_repository.get_person_by_id(id=id)

        return GetPersonSchema.model_validate(person)

    async def get_all_persons(self) -> Sequence[GetPersonSchema]:
        persons = await self._person_repository.get_all()

        return [GetPersonSchema.model_validate(person) for person in persons]
