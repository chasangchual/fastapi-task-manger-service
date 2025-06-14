import uuid
from typing import Any, Coroutine

from fastapi import APIRouter,HTTPException, Path

from model.repository import Repository
from model.task_model import NewTaskRequest, Task, AssignUserRequest
from model.user_model import User

task_router = APIRouter()
repository = Repository()

@task_router.post("/tasks")
async def add_task(new_task: NewTaskRequest) -> dict:
    repository.add_task(new_task)
    return {
        "message": "Task added",
    }

@task_router.get("/tasks")
async def get_tasks() -> list[Task]:
    return repository.find_all_tasks()

@task_router.get("/tasks/{task_public_id}")
async def get_tasks(task_public_id: str = Path(..., title="task's external identifier")) -> Task:
    task = repository.find_task_by_public_id(uuid.UUID(task_public_id))
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@task_router.post("/tasks/{task_public_id}/user")
async def add_user_to_task(request: AssignUserRequest, task_public_id: str = Path(..., title="task's external identifier")) -> Task:
    task = repository.find_task_by_public_id(uuid.UUID(task_public_id))
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if not request.user_public_id:
        raise HTTPException(status_code=400, detail="Missing user_public_id")

    user = repository.find_user_by_public_id(request.user_public_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not repository.find_user_in_task_by_public_id(task, request.user_public_id):
        task.assign_user(user)

    return task