from motor.motor_asyncio import AsyncIOMotorClient
from DTOs.create_user_dto import CreateUserDTO  # 确保路径正确
from common.security import get_password_hash

async def create_user(db: AsyncIOMotorClient, user_data: CreateUserDTO):
    """
    Create a new user in the database.

    Args:
        db (AsyncIOMotorClient): The database client.
        user_data (CreateUserDTO): The user data to create.

    Returns:
        dict: The created user data.
    """
    # 对密码进行哈希处理
    hashed_password = get_password_hash(user_data.password)
    user_dict = user_data.model_dump(exclude={"confirm_password"})
    user_dict["hashed_password"] = hashed_password

    # 将用户数据插入数据库
    await db["users"].insert_one(user_dict)

    # 返回插入的用户数据（可能需要移除敏感信息）
    created_user = await db["users"].find_one({"_id": user_dict["_id"]})
    return created_user
