from fastapi import FastAPI
from controller.task_controller import task_router
from controller.user_controller import user_router

app = FastAPI()

@app.get("/health-check")
async def root() -> dict:
    return {"message": "Hello World"}

app.include_router(task_router)
app.include_router(user_router)