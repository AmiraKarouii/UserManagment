from fastapi import APIRouter
from fastapi import Depends

from exceptions.custom_exceptions import UserCreationException, UserNotFoundException, UserNotFoundExceptionId
from helper.engine import (SessionLocal)
from sqlalchemy.orm import Session
from schemas.schemas import Response, RequestUser
import services.crud as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_user_service(request: RequestUser, db: Session = Depends(get_db)):
    try:
        user_created = crud.create_user_service(db, user=request.parameter)
        return user_created
    except Exception as e:
        raise UserCreationException from e

@router.get("/allusers")
async def get_users_service(db: Session = Depends(get_db)):
    users = crud.get_users_service(db)
    return {"users": users}

@router.patch("/update/{user_id}")
async def update_user(user_id: int, request: RequestUser, db: Session = Depends(get_db)):
    try:
        updated_user = crud.update_user_service(db, user_id=user_id, first_name=request.parameter.first_name,
                                         last_name=request.parameter.last_name, gender=request.parameter.gender,
                                         nationality=request.parameter.nationality, age=request.parameter.age)
        return updated_user
    except Exception as e:
        raise UserNotFoundException(user_id) from e


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        if crud.delete_user_service(db, user_id):
            return Response(status="Ok", code="200", message="User deleted successfully", result=None).dict(exclude_none=True)
    except Exception as e:
        raise UserNotFoundExceptionId(user_id) from e
@router.get("/users/{nationality}")
async def get_users_by_nationality_endpoint(nationality: str, db: Session = Depends(get_db)):
    try:
        users = crud.get_users_by_nationality_service(db, nationality)
        return users
    except Exception as e:
        raise UserNotFoundException(nationality) from e
