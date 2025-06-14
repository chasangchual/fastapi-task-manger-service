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


class User(BaseModel):
    id: int
    public_id: uuid.UUID
    email: str
    full_name: str
    status: UserStatus
    created_at: datetime
    updated_at: datetime

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
