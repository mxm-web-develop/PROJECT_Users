# controllers/users_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from common.db_session import get_db
from services.users_service import create_user
from dtos.user_dto import UserCreate, User

router = APIRouter()

@router.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    return db_user

# 更多路由...
