import os


class DevelopmentConfig:

    # Flask
    DEBUG = True
    SECRET_KEY = os.urandom(24)

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/database?charset=utf8mb4'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'p@ssw0rd'),
        'host': os.getenv('DB_HOST', 'example-db'),
        'port': os.getenv('DB_PORT', '3306')
    })

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
