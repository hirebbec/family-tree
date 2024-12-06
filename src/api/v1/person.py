from fastapi import APIRouter, status, Depends

from schemas.person import CreatePersonSchema
from services.person import PersonService

router = APIRouter(prefix="/person", tags=["Persons"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_user(
    person: CreatePersonSchema, person_service: PersonService = Depends()
) -> None:
    await person_service.create_person(person=person)
