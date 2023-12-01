# models/user_model.py
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from enum import Enum
from common import Base
import uuid

class UserRole(Enum):
    Owner = "Owner"
    Guest = "Guest"
    Sponsor = "Sponsor"
    Registrant = "Registrant"


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=True)
