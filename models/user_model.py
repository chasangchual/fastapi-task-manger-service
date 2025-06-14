import uuid
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class UserStatus(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"


class NewUserRequest(BaseModel):
    email: str
    full_name: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "sangchual.cha@gmail.com",
                "full_name": "Sangchual Cha"
            }
        }


class User(BaseModel):
    id: int
    public_id: uuid.UUID
    email: str
    full_name: str
    status: UserStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "public_id": "7a621be8-7d6a-4398-8644-300d5e9829f2",
                "email": "sangchual.cha@gmail.com",
                "full_name": "Sangchual Cha",
                "status": "ACTIVE",
                "created_at": "2025-06-14T17:42:57.548042",
                "updated_at": "2025-06-14T17:42:57.548042"
            }
        }

    @classmethod
    def create(cls, id: int, new_user: NewUserRequest) -> "User":
        now = datetime.now()
        return cls(
            id=id,
            public_id=uuid.uuid4(),
            email=new_user.email,
            full_name=new_user.full_name,
            status=UserStatus.ACTIVE,
            created_at=now,
            updated_at=now
        )
