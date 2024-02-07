from sqlalchemy import Column, String, Integer
from helper.engine import Base


class User(Base):
    __tablename__ = "users"

    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    gender=Column(String)
    age=Column(Integer)
    nationality=Column(String)


