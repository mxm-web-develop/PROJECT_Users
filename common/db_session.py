from motor.motor_asyncio import AsyncIOMotorClient
class DataBase:
  client: AsyncIOMotorClient = NotADirectoryError

db = DataBase()

def get_database() -> DataBase:
    return db