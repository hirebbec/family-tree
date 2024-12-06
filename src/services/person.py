from fastapi import Depends

from db.repository.person import PersonRepository
from schemas.person import CreatePersonSchema
from services.base import BaseService


class PersonService(BaseService):
    def __init__(self, person_repository: PersonRepository = Depends()):
        self._person_repository = person_repository

    async def create_person(self, person: CreatePersonSchema) -> None:
        await self._person_repository.create_person(person=person)
