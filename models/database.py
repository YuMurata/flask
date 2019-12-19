from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

databese_file = str(Path(__file__) / 'onegai.db')
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)
