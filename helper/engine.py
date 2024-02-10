from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Configuration.config import DATABASE_URL

origins = [
    "http://localhost",
    "http://localhost:3000",
]


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
