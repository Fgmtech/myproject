
from config.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



def get_url():
    user = settings.POSTGRES_USER
    password = settings.POSTGRES_PASSWORD
    server = settings.POSTGRES_SERVER
    db = settings.POSTGRES_DATABASE
    return f'postgresql://{user}:{password}@{server}/{db}'


SQLALCHEMY_DATABASE_URI = get_url()

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
