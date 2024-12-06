import enum


class RelationshipTypeEnum(enum.Enum):
    MOTHER = "Мать"
    FATHER = "Отец"
    SISTER = "Сестра"
    BROTHER = "Брат"
    CHILD = "Ребенок"


class SexEnum(enum.Enum):
    MAN = "Мужчина"
    WOMEN = "Женщина"
