from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import UserSchema
from repository.user_repository import UserManager
from models.User import User
from helper.engine import SessionLocal

def get_db_session() -> Session:
    return SessionLocal()

def get_users_service():
    with get_db_session() as db:
        user_manager = UserManager(db)
        return user_manager.get_users()

def create_user_service(user: UserSchema):
    with get_db_session() as db:
        user_obj = User(**user.dict())
        user_manager = UserManager(db)
        return user_manager.create_user(user_obj)

def update_user_service(user_id: int, **kwargs):
    with get_db_session() as db:
        user_manager = UserManager(db)
        return user_manager.update_user(user_id, **kwargs)

def delete_user_service(user_id: int):
    with get_db_session() as db:
        user_manager = UserManager(db)
        return user_manager.delete_user(user_id)

def get_users_by_nationality_service(nationality: str) -> List[User]:
    with get_db_session() as db:
        user_manager = UserManager(db)
        return user_manager.get_users_by_nationality(nationality)


