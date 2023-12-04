from typing import Optional, List
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

async def get_users(db: AsyncIOMotorClient, user_id: Optional[str], role: Optional[str], is_active: Optional[bool], start_time: Optional[datetime], end_time: Optional[datetime]) -> List[dict]:
    """
    Retrieve users based on various filter criteria.

    Args:
        db (AsyncIOMotorClient): The database client.
        user_id (str, optional): Specific user ID to filter by.
        role (str, optional): User role to filter by.
        is_active (bool, optional): Filter by active status.
        start_time (datetime, optional): Filter users created after this time.
        end_time (datetime, optional): Filter users created before this time.

    Returns:
        List[dict]: List of user data dictionaries.
    """
    if user_id:
        user = await db["users"].find_one({"_id": user_id})
        return [user] if user else []

    query = {}
    if role:
        query["role"] = role
    if is_active is not None:
        query["is_active"] = is_active
    if start_time:
        query["created_at"] = {"$gte": start_time}
    if end_time:
        query["created_at"] = {"$lte": end_time}

    users = await db["users"].find(query).to_list(None)
    return users
