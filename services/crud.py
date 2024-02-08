from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.User import User
from schemas.schemas import UserSchema, Response
from fastapi import HTTPException

def get_User(db: Session):
    try:
        users = db.query(User).all()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching users: " + str(e))
def create_user(db: Session, user: UserSchema):
    _user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        nationality=user.nationality,
        gender=user.gender
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return Response(status="Ok", code="200", message="User created successfully", result=_user)

def update_user(db: Session, user_id: int, first_name: str, last_name: str ,
                        age: int, nationality: str , gender: str ):
    user = db.query(User).filter(User.id == user_id).first()
    if first_name is not None:
        user.first_name = first_name
    if last_name is not None:
        user.last_name = last_name
    if age is not None:
        user.age = age
    if nationality is not None:
        user.nationality = nationality
    if gender is not None:
        user.gender = gender
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return "User deleted successfully"
        else:
            return False
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while deleting user: " + str(e))


def get_users_by_nationality(db: Session, nationality: str) -> List[User]:
    try:
        nationality_normalized = nationality.capitalize()
        users = db.query(User).filter(func.lower(User.nationality) == func.lower(nationality_normalized)).all()
        if not users:
            raise HTTPException(status_code=404, detail=f"No users found with nationality {nationality_normalized}")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching users by nationality: " + str(e))
