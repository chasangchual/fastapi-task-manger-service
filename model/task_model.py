import uuid
from datetime import datetime
from typing import List

from pydantic import BaseModel
from enum import Enum

from model.user_model import User


class TasStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class NewTaskRequest(BaseModel):
    title: str
    description: str
    due_date: datetime

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
