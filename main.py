from fastapi import FastAPI
from routes.task_controller import task_router
from routes.user_controller import user_router

app = FastAPI()

@app.get("/health-check")
async def root() -> dict:
    return {"message": "Hello World"}

app.include_router(task_router)
app.include_router(user_router)