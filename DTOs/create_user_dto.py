# DTOs/create_user_dto.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class CreateUserDTO_Request(BaseModel):
    username: str = Field(..., title="Username", max_length=100)
    full_name: Optional[str] = Field(None, title="Full Name", max_length=100)
    email: EmailStr = Field(..., title="Email Address")
    password:str = Field(..., title="Password",max_length=24,min_length=6)
    confirm_password:str = Field(..., title="Password",max_length=24,min_length=6)
    # ...其他用于创建用户的字段...

    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "full_name": "John Doe",
                "email": "johndoe@example.com",
                "password":"123123",
                "confirm_password":"123123"
                # ...其他字段示例...
            }
        }

class CreateUserDTO_Response(BaseModel):
    username: str = Field(..., title="Username", max_length=100)
    full_name: Optional[str] = Field(None, title="Full Name", max_length=100)
    email: EmailStr = Field(..., title="Email Address")

    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "full_name": "John Doe",
                "email": "johndoe@example.com",
                # ...其他字段示例...
            }
        }