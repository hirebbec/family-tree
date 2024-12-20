from fastapi import Depends

from core.exceptions import (
    person_not_found_exception,
    relationship_conflict_exception,
    relationship_not_found_exception,
)
from db.models.enums import RelationshipTypeEnum, SexEnum
from db.repository.person import PersonRepository
from db.repository.relationship import RelationshipRepository
from schemas.person import GetPersonWithRelationshipTreeSchema
from schemas.relationship import CreateRelationshipSchema, UpdateRelationshipSchema
from services.base import BaseService


class RelationshipService(BaseService):
    def __init__(
        self,
        relationship_repository: RelationshipRepository = Depends(),
        person_repository: PersonRepository = Depends(),
    ):
        self._relationship_repository = relationship_repository
        self._person_repository = person_repository
        self.ids.clear()

    ids: set = set()

    async def create_relationship(self, relationship: CreateRelationshipSchema) -> None:
        if relationship.person_id == relationship.relative_id:
            raise relationship_conflict_exception

        person = await self._person_repository.get_person_by_id(id=relationship.person_id)
        relative = await self._person_repository.get_person_by_id(id=relationship.relative_id)

        if not person or not relative:
            raise person_not_found_exception

        reverse_relationship = await self.__get_reverse_relationship(relationship=relationship)

        await self._relationship_repository.create_relationship(relationship=relationship)
        await self._relationship_repository.create_relationship(relationship=reverse_relationship)

    async def get_relationship_tree_by_id(
        self, id: int, existing_id: int, relationship_type: RelationshipTypeEnum | None = None
    ) -> GetPersonWithRelationshipTreeSchema:
        person = await self._person_repository.get_person_by_id(id=id)

        if not person:
            raise person_not_found_exception

        if id in self.ids:
            person_relationships = []
        else:
            person_relationships = await self._relationship_repository.get_relationships_by_person_id(
                relative_id=id, existing_id=existing_id
            )

            self.ids.add(id)

        return GetPersonWithRelationshipTreeSchema.model_encode(
            person,
            {
                "relationships": [
                    await self.get_relationship_tree_by_id(
                        person_relationship.person_id,
                        existing_id=id,
                        relationship_type=person_relationship.relationship_type,
                    )
                    for person_relationship in person_relationships
                    if person_relationship.person_id not in self.ids
                ]
            },
            {
                "relationship_type": relationship_type,
            },
        )

    async def update_relationship_by_id(self, id: int, relationship: UpdateRelationshipSchema) -> None:
        if not await self._relationship_repository.get_relationship_by_id(id=id):
            raise relationship_not_found_exception

        await self._relationship_repository.update_relationship_by_id(id=id, relationship=relationship)

        relationship = await self._relationship_repository.get_relationship_by_id(id=id)
        reverse_relationship = await self.__get_reverse_relationship(
            relationship=CreateRelationshipSchema.model_encode(relationship)
        )

        await self._relationship_repository.update_relationship(relationship=reverse_relationship)

    async def delete_relationship_by_id(self, id: int) -> None:
        relationship = await self._relationship_repository.get_relationship_by_id(id=id)

        if not relationship:
            raise relationship_not_found_exception

        await self._relationship_repository.delete_relationship_by_id(id=id)
        await self._relationship_repository.delete_relationship_by_person_id_and_relative_id(
            person_id=relationship.relative_id, relative_id=relationship.person_id
        )

    async def __get_reverse_relationship(self, relationship: CreateRelationshipSchema) -> CreateRelationshipSchema:
        relative_sex = (await self._person_repository.get_person_by_id(id=relationship.relative_id)).sex

        if (
            relationship.relationship_type == RelationshipTypeEnum.MOTHER
            or relationship.relationship_type == RelationshipTypeEnum.FATHER
        ):
            reverse_type = RelationshipTypeEnum.CHILD
        elif relationship.relationship_type == RelationshipTypeEnum.CHILD:
            reverse_type = RelationshipTypeEnum.MOTHER if relative_sex == SexEnum.WOMEN else RelationshipTypeEnum.FATHER
        else:
            reverse_type = (
                RelationshipTypeEnum.SISTER if relative_sex == SexEnum.WOMEN else RelationshipTypeEnum.BROTHER
            )

        return CreateRelationshipSchema(
            person_id=relationship.relative_id,
            relative_id=relationship.person_id,
            relationship_type=reverse_type.value,
        )
