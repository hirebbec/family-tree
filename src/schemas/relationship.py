from db.models.enums import RelationshipTypeEnum
from schemas.base import BaseSchema


class CreateRelationshipSchema(BaseSchema):
    person_id: int
    relative_id: int
    relationship_type: RelationshipTypeEnum


class GetRelationshipSchema(CreateRelationshipSchema):
    id: int
