from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional

class GetUserDTO(BaseModel):
    id: Optional[str] = Field(None, title="User ID")

class UserPublic(BaseModel):
    username: str
    full_name: Optional[str]
    email: EmailStr
    avator:str
    # ...其他非敏感信息...

class UserOwner(UserPublic):
    is_active: bool
    # ...其他敏感信息...

    class Config:
        orm_mode = True