from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  # MongoDB 默认使用 "_id"
    username: str = Field(..., title="Username", max_length=100)
    full_name: Optional[str] = Field(None, title="Full Name", max_length=100)
    email: EmailStr = Field(..., title="Email Address")
    is_active: bool = Field(True, title="Is Active")
    avator:Optional[str] = Field(None, title="avator")
    # ...其他字段...

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "full_name": "John Doe",
                "email": "johndoe@example.com",
                "is_active": True,
                "avator":"www.myavator.com/123221.jpg"
                # ...其他字段示例...
            }
        }

# class UserInDB(User):
#     hashed_password: Optional[str] = Field(None, title="Hashed Password")