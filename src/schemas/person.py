from typing import Sequence

from db.models.enums import SexEnum, RelationshipTypeEnum
from schemas.base import BaseSchema


class CreatePersonSchema(BaseSchema):
    name: str
    surname: str
    patronymic: str
    Sex: SexEnum


class GetPersonSchema(CreatePersonSchema):
    id: int


class GetPersonWithRelationshipTreeSchema(GetPersonSchema):
    relationship_type: RelationshipTypeEnum | None = None
    relationships: Sequence["GetPersonWithRelationshipTreeSchema"]
