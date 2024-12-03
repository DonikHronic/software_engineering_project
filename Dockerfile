ARG PYTHON_VERSION=3.11.10
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN  poetry install --no-root --no-interaction --no-ansi
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ./docker-entrypoint.sh