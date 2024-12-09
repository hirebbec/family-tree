from typing import Sequence

from fastapi import Depends

from core.exceptions import person_not_found_exception
from db.repository.person import PersonRepository
from db.repository.relationship import RelationshipRepository
from schemas.person import CreatePersonSchema, GetPersonSchema, UpdatePersonSchema
from services.base import BaseService


class PersonService(BaseService):
    def __init__(
        self,
        person_repository: PersonRepository = Depends(),
        relationship_repository: RelationshipRepository = Depends(),
    ):
        self._person_repository = person_repository
        self._relationship_repository = relationship_repository

    async def create_person(self, person: CreatePersonSchema) -> None:
        await self._person_repository.create_person(person=person)

    async def get_person_by_id(self, id: int) -> GetPersonSchema:
        person = await self._person_repository.get_person_by_id(id=id)

        if not person:
            raise person_not_found_exception

        return GetPersonSchema.model_validate(person)

    async def get_all_persons(self) -> Sequence[GetPersonSchema]:
        persons = await self._person_repository.get_all()

        return [GetPersonSchema.model_validate(person) for person in persons]

    async def update_person_by_id(self, id: int, person: UpdatePersonSchema) -> None:
        if not await self._person_repository.get_person_by_id(id=id):
            raise person_not_found_exception

        await self._person_repository.update_person_by_id(id=id, person=person)

    async def delete_person_by_id(self, id: int) -> None:
        if not await self._person_repository.get_person_by_id(id=id):
            raise person_not_found_exception

        await self._person_repository.delete_person_by_id(id=id)
        await self._relationship_repository.delete_relationships_by_person_id(person_id=id)
        await self._relationship_repository.delete_relationships_by_relative_id(relative_id=id)
