FROM python:3.8

WORKDIR /web

COPY Pipfile Pipfile

RUN pip install pipenv &&\
    pipenv shell &&\
    pipenv install &&\
    flask db init &&\
    flask db migrate &&\
    flask db upgrade

