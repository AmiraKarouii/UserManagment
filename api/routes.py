from fastapi import APIRouter, HTTPException
from fastapi import Depends
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
    crud.create_user(db, user=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="User created successfully").dict(exclude_none=True)

@router.get("/allusers")
async def get_user(db: Session = Depends(get_db)):
    users = crud.get_User(db)
    return {"users": users}

@router.patch("/update/{user_id}")
async def update_user(user_id: int, request: RequestUser, db: Session = Depends(get_db)):
    _user = crud.update_user(db, user_id=user_id, first_name=request.parameter.first_name,
                             last_name=request.parameter.last_name, gender=request.parameter.gender, nationality=request.parameter.nationality,
                             age=request.parameter.age)
    return _user

@router.delete("/delete/{user_id}")
async def delete_user(user_id: int,  db: Session = Depends(get_db)):
    crud.remove_user(db, user_id=user_id)
    return "Success delete user"

@router.get("/users/{nationality}")
async def get_users_by_nationality_endpoint(nationality: str, db: Session = Depends(get_db)):
    users = crud.get_users_by_nationality(db, nationality)
    return users