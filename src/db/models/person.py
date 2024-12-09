from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from db.models import BaseModel
from db.models.enums import SexEnum
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin


class Person(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "persons"

    name: Mapped[str] = mapped_column(String, nullable=False, unique=False)
    surname: Mapped[str] = mapped_column(String, nullable=False, unique=False)
    patronymic: Mapped[str] = mapped_column(String, nullable=False, unique=False)
    sex: Mapped[SexEnum] = mapped_column(Enum(SexEnum), nullable=False, unique=False)
