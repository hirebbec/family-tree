FROM python:3.12-alpine

WORKDIR /usr/family-tree/src

ENV PYTHONUNBUFFERED=1 \
    TZ="Europe/Moscow"

RUN apk add --no-cache curl && \
    pip install --upgrade pip --no-cache-dir && \
    pip install poetry --no-cache-dir

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-cache

COPY . .
