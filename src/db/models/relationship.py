from sqlalchemy import Integer, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.enums import RelationshipTypeEnum
from db.models.mixins import CreatedAtMixin, UpdatedAtMixin, IDMixin


class Relationship(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "relationships"

    person_id: Mapped[int] = mapped_column(Integer, nullable=False)
    relative_id: Mapped[int] = mapped_column(Integer, nullable=False)
    relationship_type: Mapped[RelationshipTypeEnum] = mapped_column(Enum(RelationshipTypeEnum), nullable=False)

    __table_args__ = (UniqueConstraint("person_id", "relative_id"), {})
