import os


class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(24)

    # Flask

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/database?charset=utf8mb4'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'p@ssw0rd'),
        'host': os.getenv('DB_HOST', 'example-db'),
        'port': os.getenv('DB_PORT', '3306')
    })

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DebugConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class LocalConfig(DebugConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db'


def get_config(config_name: str) -> str:
    base_route = 'application.config.'
    config_dict = {
        'default': base_route+'Config',
        'debug': base_route+'DebugConfig',
        'local': base_route+'LocalConfig'
    }
    return config_dict[config_name]
