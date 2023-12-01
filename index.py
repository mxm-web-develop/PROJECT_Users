from fastapi import FastAPI
from .common.db_session import engine, Base
from .models.user_model import User
from .controllers import users_controller, auth_controller

# 创建FastAPI应用实例
app = FastAPI()

# 创建数据库表（如果尚不存在）
Base.metadata.create_all(bind=engine)

# 注册路由控制器
app.include_router(users_controller.router)
app.include_router(auth_controller.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the User Manager Service"}
