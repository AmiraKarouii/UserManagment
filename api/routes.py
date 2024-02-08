from fastapi import APIRouter, HTTPException
from fastapi import Depends
from helper.engine import (SessionLocal)
from sqlalchemy.orm import Session
from schemas.schemas import Response, RequestUser, UserSchema
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
    user_created = crud.create_user(db, user=request.parameter)
    return user_created.dict(exclude_none=True)

@router.get("/allusers")
async def get_user(db: Session = Depends(get_db)):
    users = crud.get_User(db)
    return {"users": users}

@router.patch("/update/{user_id}")
async def update_user(user_id: int, request: RequestUser, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id=user_id, first_name=request.parameter.first_name,
                                     last_name=request.parameter.last_name, gender=request.parameter.gender,
                                     nationality=request.parameter.nationality, age=request.parameter.age)

    return updated_user

@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id)
    if deleted_user:
        return Response(status="Ok", code="200", message="User deleted successfully", result= None).dict(exclude_none=True)
    else:
        raise HTTPException(status_code=404, detail="User with the specified ID does not exist")

@router.get("/users/{nationality}")
async def get_users_by_nationality_endpoint(nationality: str, db: Session = Depends(get_db)):
    users = crud.get_users_by_nationality(db, nationality)
    return users