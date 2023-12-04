from motor.motor_asyncio import AsyncIOMotorClient

async def disable_user(db: AsyncIOMotorClient, user_id: str, is_active: bool):
    """
    Enable or disable a user account.
    Args:
        db (AsyncIOMotorClient): The database client.
        user_id (str): Unique ID of the user to be enabled/disabled.
        is_active (bool): New status of the user's account.

    Returns:
        dict: Information about the operation.
    """
    db['s']
    await db["users"].update_one({"_id": user_id}, {"$set": {"is_active": is_active}})
    return await db["users"].find_one({"_id": user_id})
