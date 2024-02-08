# from typing import List
# from sqlalchemy import func
# from sqlalchemy.orm import Session
# from models.User import User
# from schemas.schemas import UserSchema, Response
# from exceptions.custom_exceptions import UserNotFoundException, UserUpdateException, \
#     UserCreationException, UserNotFoundExceptionId
#
#
# def get_User(db: Session):
#     users = db.query(User).all()
#     return users
#
# def create_user(db: Session, user: UserSchema):
#         _user = User(
#             first_name=user.first_name,
#             last_name=user.last_name,
#             age=user.age,
#             nationality=user.nationality,
#             gender=user.gender
#         )
#         db.add(_user)
#         db.commit()
#         db.refresh(_user)
#         return Response(status="Ok", code="200", message="User created successfully", result=_user)
#
#
# def update_user(db: Session, user_id: int, first_name: str, last_name: str,
#                 age: int, nationality: str, gender: str):
#     user = db.query(User).filter(User.id == user_id).first()
#
#     if first_name is not None:
#         user.first_name = first_name
#     if last_name is not None:
#         user.last_name = last_name
#     if age is not None:
#         user.age = age
#     if nationality is not None:
#         user.nationality = nationality
#     if gender is not None:
#         user.gender = gender
#     db.commit()
#     db.refresh(user)
#     return user
#
#
# def delete_user(db: Session, user_id: int):
#     user = db.query(User).filter(User.id == user_id).first()
#     db.delete(user)
#     db.commit()
#     return "User deleted successfully"
#
# def get_users_by_nationality(db: Session, nationality: str) -> List[User]:
#     nationality_normalized = nationality.capitalize()
#     users = db.query(User).filter(func.lower(User.nationality) == func.lower(nationality_normalized)).all()
#     return users


# services/user_service.py

from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import UserSchema, Response
from repository.user_repository import get_users, create_user, update_user, delete_user, get_users_by_nationality
from models.User import User

def get_users_service(db: Session):
    return get_users(db)

def create_user_service(db: Session, user: UserSchema):
    user_obj = User(**user.dict())
    return create_user(db, user_obj)

def update_user_service(db: Session, user_id: int, **kwargs):
    updated_user = update_user(db, user_id, **kwargs)

    return updated_user


def delete_user_service(db: Session, user_id: int):
    return delete_user(db, user_id)


def get_users_by_nationality_service(db: Session, nationality: str) -> List[User]:
    return get_users_by_nationality(db, nationality)
