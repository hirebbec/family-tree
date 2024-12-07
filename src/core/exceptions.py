from fastapi import HTTPException
from starlette import status


class ModelEncodeValidationError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


person_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Person not found",
)

relationship_conflict_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Relationship conflict",
)
