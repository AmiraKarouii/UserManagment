from sqlalchemy import func
from typing import List
from sqlalchemy.orm import Session
from models.User import User

def get_users(db: Session) -> List[User]:
    return db.query(User).all()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user_id: int, **kwargs):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for attr, value in kwargs.items():
            setattr(user, attr, value)
        db.commit()
        db.refresh(user)
        return user
    else:
        return None

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return True



def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_users_by_nationality(db: Session, nationality: str) -> List[User]:
    nationality_normalized = nationality.capitalize()
    return db.query(User).filter(func.lower(User.nationality) == func.lower(nationality_normalized)).all()