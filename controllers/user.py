from typing import Optional
from fastapi import APIRouter, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from common.db_session import get_database
from DTOs.user_dot import UserCreate, UserResponse  # 假设UserRead是用于读取的DTO
from bson import ObjectId
from common.security import get_password_hash

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_new_user(user: UserCreate):
    db: AsyncIOMotorClient = get_database().client
    # 检查用户是否已存在
    existing_user = await db["users"].find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # 创建新用户
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict.update({"hashed_password": hashed_password})
    del user_dict["password"]  # 删除原始密码

    # 插入新用户到数据库
    result = await db["users"].insert_one(user_dict)
    created_user = await db["users"].find_one({"_id": result.inserted_id})
    return created_user

@router.get("/users/", response_model=list[UserResponse])
async def read_user(user_id: Optional[str] = None):
    db: AsyncIOMotorClient = get_database().client
    if user_id:
        # 将字符串ID转换为ObjectId
        oid = ObjectId(user_id)
        user = await db["users"].find_one({"_id": oid})
        return [user] if user else []
    else:
        users = await db["users"].find().to_list(None)
        return users