from db.models.enums import SexEnum
from schemas.base import BaseSchema


class CreateRelationshipSchema(BaseSchema):
    person_id: int
    relative_id: int
    relationship_type: str


class GetRelationshipSchema(CreateRelationshipSchema):
    id: int
