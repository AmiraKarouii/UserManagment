from typing import Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


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
    code: Optional[str]
    status: Optional[str]
    message: Optional[str]
    result: Optional[T]


