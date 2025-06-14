import uuid
from datetime import datetime
from typing import List

from pydantic import BaseModel
from enum import Enum

from models.user_model import User


class TasStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class NewTaskRequest(BaseModel):
    title: str
    description: str
    due_date: datetime

    class Config:
        json_schema_extra = {
            "title": "Clean up the member sign up logs",
            "description": "scheduled weekly tasks cleaning up the member sign up logs",
            "due_date": "2025-06-27"
        }


class AssignUserRequest(BaseModel):
    user_public_id: uuid.UUID


class Task(BaseModel):
    id: int
    public_id: uuid.UUID
    title: str
    description: str
    status: TasStatus
    due_date: datetime
    created_at: datetime
    updated_at: datetime
    users: List[User] = []

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "public_id": "0ed65746-bc2d-4f72-8e5a-c8488231b587",
                "title": "Clean up the member sign up logs",
                "description": "scheduled weekly tasks cleaning up the member sign up logs",
                "status": "PENDING",
                "due_date": "2025-06-27T00:00:00",
                "created_at": "2025-06-14T17:49:54.892957",
                "updated_at": "2025-06-14T17:49:54.892957",
                "users": [
                    {
                        "id": 1,
                        "public_id": "fd78c9e9-9206-45df-bd15-92437ff253b1",
                        "email": "sangchual.cha@gmail.com",
                        "full_name": "Sangchual Cha",
                        "status": "ACTIVE",
                        "created_at": "2025-06-14T17:49:54.889812",
                        "updated_at": "2025-06-14T17:49:54.889812"
                    }
                ]
            }
        }

    @classmethod
    def create(cls, id: int, new_request: NewTaskRequest):
        now = datetime.now()
        return cls(
            id=id,
            public_id=uuid.uuid4(),
            title=new_request.title,
            description=new_request.description,
            status=TasStatus.PENDING,
            due_date=new_request.due_date,
            created_at=now,
            updated_at=now
        )

    def assign_user(self, user: User):
        self.users.append(user)
