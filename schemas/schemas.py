from typing import Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

"""""""""
LEARNING TIPS:

Models Vs Schemas while they do sound the same as in defining and handling data structure 
but they have different purposes in the process of developing a FastAPI Application.

Schemas are used for data validation and serialization/deserialization of request and response bodies
they are defined using pydantic which is a data validation library it defines how data should be formatted
in http requests for example having data types, constraints and validation rules  

and Models they are used to define the structure of the applications data on a database level 
they represent the data at a database level they are defined using the ORM library such as SQLAlchemy
they define the structure of the data stored in the database including relations between entities, and database constraints.

"""""""""


class UserSchema(BaseModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    nationality: Optional[str] = None
    gender: Optional[str] = None

    class Config:
        orm_mode = True



class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


