from typing import List

from sqlalchemy.orm import Session
from models.User import User
from schemas.schemas import UserSchema, Response
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def get_User(db: Session):
    try:
        users = db.query(User).all()
        return users
    except Exception as e:
        # Log the error or perform any other necessary actions
        raise HTTPException(status_code=500, detail="An error occurred while fetching users: " + str(e))

def get_user_by_id(db: Session, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return Response(status="Ok", content={"user": user})
        else:
            raise HTTPException(status_code=404, detail="User with the specified ID does not exist")
    except Exception as e:
        # Log the error or perform any other necessary actions
        raise HTTPException(status_code=500, detail="An error occurred while fetching user by ID: " + str(e))

def create_user(db: Session, user: UserSchema):
    try:
        if not all(user):
            raise ValueError("One or more required fields are missing")
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
        return Response(status="Created", content={"result": {"code": "200", "message": "User created successfully", "user": _user}})
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="One or more fields violate uniqueness constraints")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while creating user you have missing fields" )


def update_user(db: Session, user_id: int, first_name: str, last_name: str, age: int, nationality: str, gender: str):
    try:
        if not user_id:
            raise ValueError("User ID must be specified")
        _user = get_user_by_id(db=db, user_id=user_id)
        if not _user:
            raise HTTPException(status_code=404, detail="User with the specified ID does not exist")

        # Update user fields if not None
        if first_name is not None:
            _user.first_name = first_name
        if last_name is not None:
            _user.last_name = last_name
        if age is not None:
            _user.age = age
        if nationality is not None:
            _user.nationality = nationality
        if gender is not None:
            _user.gender = gender

        db.commit()
        db.refresh(_user)
        return Response(status="Ok", content={"message": "User updated successfully", "user": _user})
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # Log the error or perform any other necessary actions
        raise HTTPException(status_code=500, detail="An error occurred while updating user: " + str(e))


def remove_user(db: Session, user_id: int):
    try:
        if not user_id:
            raise ValueError("User ID must be specified")
        _user = get_user_by_id(db=db, user_id=user_id)
        if not _user:
            raise HTTPException(status_code=404, detail="User with the specified ID does not exist")

        db.delete(_user)
        db.commit()
        return Response(status="Ok", content={"message": "User deleted successfully"})
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # Log the error or perform any other necessary actions
        raise HTTPException(status_code=500, detail="An error occurred while deleting user")


def get_users_by_nationality(db: Session, nationality: str) -> List[User]:
    try:
        users = db.query(User).filter(User.nationality == nationality).all()
        if not users:
            raise HTTPException(status_code=404, detail=f"No users found with nationality {nationality}")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching users by nationality: " + str(e))
