from db.models.enums import RelationshipTypeEnum
from schemas.base import BaseSchema


class UpdateRelationshipSchema(BaseSchema):
    relationship_type: RelationshipTypeEnum


class CreateRelationshipSchema(UpdateRelationshipSchema):
    person_id: int
    relative_id: int
