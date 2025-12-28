from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database
from app.crud.task import get_tasks_by_project, get_task, create_task, update_task, delete_task
from app.routers.auth import get_current_user

router = APIRouter()

@router.get("/projects/{project_id}/tasks")
def read_tasks(project_id: int, db: Session = Depends(database.get_db)):
    return get_tasks_by_project(db, project_id)

@router.post("/projects/{project_id}/tasks")
def create_new_task(
    project_id: int, 
    task: schemas.TaskCreate, 
    db: Session = Depends(database.get_db), 
    current_user=Depends(get_current_user)
):
    return create_task(db, project_id, task, current_user.id)

@router.get("/{task_id}")
def read_task(task_id: int, db: Session = Depends(database.get_db)):
    return get_task(db, task_id)

@router.put("/{task_id}")
def update_existing_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    return update_task(db, task_id, task)

@router.delete("/{task_id}")
def delete_task_route(task_id: int, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    # si delete_task nécessite owner_id, passe current_user.id
    result = delete_task(db, task_id, current_user.id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found or not authorized")
    return result
