from typing import Sequence

from db.models.enums import SexEnum, RelationshipTypeEnum
from schemas.base import BaseSchema


class UpdatePersonSchema(BaseSchema):
    name: str
    surname: str
    patronymic: str
    sex: SexEnum


class CreatePersonSchema(UpdatePersonSchema): ...


class GetPersonSchema(CreatePersonSchema):
    id: int


class GetPersonWithRelationshipTreeSchema(GetPersonSchema):
    relationship_type: RelationshipTypeEnum | None = None
    relationships: Sequence["GetPersonWithRelationshipTreeSchema"]
