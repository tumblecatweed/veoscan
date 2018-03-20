import os

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String
from sqlalchemy import Text


DB_URL = os.environ.get('VEOSCAN_DB_URL')
assert DB_URL is not None
engine = create_engine(DB_URL)
meta = MetaData()
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()


class Peer(Base):
    __tablename__ = 'peer'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    height = Column(Integer)
    description = Column(Text)
    updated_at = Column(DateTime)

    def __init__(self, url):
        self.url = url


def init_db():
    Base.metadata.create_all(engine)
