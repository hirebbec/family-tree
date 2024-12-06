from sqlalchemy.orm import DeclarativeBase, declarative_mixin


@declarative_mixin
class BaseModel(DeclarativeBase): ...
