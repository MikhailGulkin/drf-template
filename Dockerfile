# pull official base image
FROM python:3.10

# set work directory
WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PROD 0

# install dependencies

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false

RUN poetry install --without dev

# copy project
COPY ./src ./src

