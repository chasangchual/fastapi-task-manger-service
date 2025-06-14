import uuid
from typing import List

from model.user_model import User, NewUserRequest
from model.task_model import NewTaskRequest, Task

class Repository(object):
    users: List[User] = []
    tasks: List[Task] = []
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Repository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.users = []
        self.tasks = []

    def add_user(self, new_user: NewUserRequest):
        if not self.find_user_by_email(new_user.email):
            self.users.append(User.create(len(self.users) + 1,  new_user))

    def find_all_users(self) -> List[User]:
        return self.users

    def find_user_by_email(self, email: str) -> User | None:
        for user in self.users:
            if user.email == email:
                return user
        return None

    def find_user_by_public_id(self, public_id: uuid.UUID) -> User | None:
        for user in self.users:
            if user.public_id == public_id:
                return user
        return None

    def add_task(self, new_task: NewTaskRequest, user: User = None):
        if user and self.find_user_by_email(user.email) is None:
            raise KeyError(f'{user.email} is not registered')

        self.tasks.append(Task.create(len(self.tasks) + 1,  new_task))

        if user is not None:
            self.tasks[-1].assign_user(user)

    def find_all_tasks(self) -> List[Task]:
        return self.tasks

    def find_task_by_public_id(self, public_id: uuid.UUID) -> Task | None:
        for task in self.tasks:
            if task.public_id == public_id:
                return task
        return None

    def find_user_in_task_by_public_id(self, task:Task, public_id: uuid.UUID) -> User | None:
        for user in task.users:
            if user.public_id == public_id:
                return user
        return None
