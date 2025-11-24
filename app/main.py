from fastapi import FastAPI
from app.routers import auth, users, projects, tasks, comments
from fastapi.staticfiles import StaticFiles
from app.models import User
app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router, prefix="/users")
app.include_router(projects.router, prefix="/projects")
app.include_router(tasks.router, prefix="/tasks")
app.include_router(comments.router, prefix="/comments")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
