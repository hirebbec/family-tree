from db.models.enums import SexEnum
from schemas.base import BaseSchema


class CreatePersonSchema(BaseSchema):
    name: str
    surname: str
    patronymic: str
    Sex: SexEnum


class GetUserSchema(CreatePersonSchema):
    id: int
