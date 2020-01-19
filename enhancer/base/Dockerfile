FROM python:3.8

WORKDIR /enhancer

COPY Pipfile ./

RUN pip install pipenv &&\
    pipenv install --system --skip-lock

