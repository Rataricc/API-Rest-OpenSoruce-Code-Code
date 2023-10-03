from sqlmodel import create_engine, Session
from sqlalchemy.ext.declarative import declarative_base
import os

DEBUG = os.getenv("DEBUG", default=True)
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)
database = declarative_base

def get_session():
    with Session(engine) as session:
        yield session