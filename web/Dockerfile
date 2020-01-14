FROM python:3.8

WORKDIR /web

RUN pipenv shell &&\
    pipenv install &&\
    flask db init &&\
    flask db migrate &&\
    flask db upgrade

