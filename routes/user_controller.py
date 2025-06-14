import uuid

from fastapi import APIRouter, HTTPException, Path

from models.repository import Repository
from models.task_model import Task
from models.user_model import User, NewUserRequest

user_router = APIRouter()

repository = Repository()


@user_router.post("/users", status_code=201)
async def add_user(new_user: NewUserRequest) -> dict:
    repository.add_user(new_user)
    return {
        "message": "Task added",
    }

@user_router.get("/users")
async def get_users() -> list[User]:
    return repository.find_all_users()

@user_router.get("/users/{user_public_id}")
async def get_users(user_public_id: str = Path(..., title="user's external identifier")) -> User:
    user = repository.find_user_by_public_id(uuid.UUID(user_public_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
