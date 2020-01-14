FROM python:3.8

ENTRYPOINT [ "bash", "-c" ]

CMD ["cd","flask", "&&",\
    " pip"," install", "pipenv", "&&",\
    "pipenv","install", "&&",\
    "pipenv", "shell", "&&",\
    "flask", "db", "init", "&&",\
    "flask", "db", "migrate", "&&",\
    "flask", "db", "upgrade", "&&",\
    "python", "run.py"]