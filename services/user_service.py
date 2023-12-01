# services/users_service.py
from sqlalchemy.orm import Session
from common import get_password_hash
from models.user_model import User
from DTOs.user_dto import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict(),
                   hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 更多函数...
