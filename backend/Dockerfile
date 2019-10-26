FROM python:3.7

WORKDIR /usr/src/app

RUN pip install --upgrade pip poetry

COPY ./backend ./backend
COPY ./poetry.lock ./pyproject.toml ./

RUN ["poetry", "config", "settings.virtualenvs.create", "false"]
RUN ["poetry", "install"]

EXPOSE 5000
