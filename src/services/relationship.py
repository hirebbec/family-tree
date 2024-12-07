from fastapi import Depends

from core.exceptions import person_not_found_exception, relationship_conflict_exception
from db.models.enums import RelationshipTypeEnum, SexEnum
from db.repository.person import PersonRepository
from db.repository.relationship import RelationshipRepository
from schemas.relationship import CreateRelationshipSchema
from services.base import BaseService


class RelationshipService(BaseService):
    def __init__(
        self,
        relationship_repository: RelationshipRepository = Depends(),
        person_repository: PersonRepository = Depends(),
    ):
        self._relationship_repository = relationship_repository
        self._person_repository = person_repository

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

    async def __get_reverse_relationship(self, relationship: CreateRelationshipSchema) -> CreateRelationshipSchema:
        relative_sex = (await self._person_repository.get_person_by_id(id=relationship.relative_id)).Sex

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
