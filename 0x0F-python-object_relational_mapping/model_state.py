#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql://<username>:<password>@localhost:3306/<db_name>', echo=True)

if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker

    Base.metadata.create_all(engine)
