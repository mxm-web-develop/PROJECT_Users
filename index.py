from fastapi import FastAPI
from contextlib import asynccontextmanager
from common import db, get_database
from controllers.user import router as users_controller
from motor.motor_asyncio import AsyncIOMotorClient
# 创建FastAPI应用实例
app = FastAPI()

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # 应用启动时的操作
    db.client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")
    yield
    # 应用关闭时的操作
    db.client.close()

# 注册路由控制器
app.include_router(users_controller)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the User Manager Service"}
