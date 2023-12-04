from fastapi import APIRouter, Query, HTTPException, Body, Path
from typing import List, Optional
from datetime import datetime
from DTOs.create_user_dto import CreateUserDTO_Response, CreateUserDTO_Request
from services import create_user, delete_user, get_users, update_user
from common.db_session import get_database
from motor.motor_asyncio import AsyncIOMotorClient

router = APIRouter()

@router.post("/users/", response_model=CreateUserDTO_Response, summary="Create a new user")
async def create_new_user(user: CreateUserDTO_Request = Body(...)):
    """
    Create a new user with the provided information.
    """
    db = get_database().client
    return await create_user(db, user)


@router.get("/users/", response_model=List[UserResponse], summary="Retrieve users")
async def read_users(user_id: Optional[str] = Query(None), role: Optional[str] = Query(None), is_active: Optional[bool] = Query(None), start_time: Optional[datetime] = Query(None), end_time: Optional[datetime] = Query(None)):
    """
    Retrieve users with optional filtering by ID, role, activity status, and creation time range.
    """
    db = get_database().client
    return await get_users(db, user_id,role, is_active, start_time, end_time)

@router.put("/users/{user_id}", response_model=UserResponse, summary="Update a user's information")
async def update_user_info(user_id: str = Path(...), user: UserUpdate = Body(...)):
    """
    Update the information of a specific user.
    """
    db = get_database().client
    return await update_user(db, user_id, user)

@router.delete("/users/{user_id}", response_model=UserResponse, summary="Delete a user")
async def delete_user(user_id: str = Path(...)):
    """
    Delete a specific user by their unique ID.
    """
    db = get_database().client
    return await delete_user(db, user_id)
