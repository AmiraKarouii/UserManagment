from sqlalchemy import func
from typing import List
from sqlalchemy.orm import Session
from models.User import User

class UserManager:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self) -> List[User]:
        return self.db.query(User).all()

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id: int, **kwargs):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            for attr, value in kwargs.items():
                setattr(user, attr, value)
            self.db.commit()
            self.db.refresh(user)
            return user
        else:
            return None

    def delete_user(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        self.db.delete(user)
        self.db.commit()
        return True

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_users_by_nationality(self, nationality: str) -> List[User]:
        nationality_normalized = nationality.capitalize()
        return self.db.query(User).filter(func.lower(User.nationality) == func.lower(nationality_normalized)).all()

