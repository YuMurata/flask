FROM python:3.8

WORKDIR /web

COPY Pipfile ./

RUN pip install pipenv &&\
    pipenv install --system --skip-lock

