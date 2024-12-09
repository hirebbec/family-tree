from typing import Sequence

from fastapi import APIRouter, status, Depends


from schemas.person import CreatePersonSchema, GetPersonSchema, UpdatePersonSchema
from services.person import PersonService

router = APIRouter(prefix="/person", tags=["Persons"])


@router.get("/all", status_code=status.HTTP_200_OK, response_model=Sequence[GetPersonSchema])
async def get_all_persons(
    person_service: PersonService = Depends(),
) -> Sequence[GetPersonSchema]:
    return await person_service.get_all_persons()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=GetPersonSchema)
async def get_person_by_id(id: int, person_service: PersonService = Depends()) -> GetPersonSchema:
    return await person_service.get_person_by_id(id=id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_person(person: CreatePersonSchema, person_service: PersonService = Depends()) -> None:
    await person_service.create_person(person=person)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=None)
async def update_person_by_id(id: int, person: UpdatePersonSchema, person_service: PersonService = Depends()) -> None:
    await person_service.update_person_by_id(id=id, person=person)


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=None)
async def delete_person_by_id(id: int, person_service: PersonService = Depends()) -> None:
    await person_service.delete_person_by_id(id=id)
