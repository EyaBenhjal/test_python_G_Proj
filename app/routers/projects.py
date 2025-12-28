from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, schemas
from app.crud.project import create_project, get_all_projects, get_project, update_project, delete_project
from app.routers.auth import get_current_user
from app import crud

router = APIRouter()

@router.get("/")
def read_projects(db: Session = Depends(database.get_db)):
    return get_all_projects(db)

@router.post("/")
def create_project_endpoint(project: schemas.ProjectCreate, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    return create_project(db, project, current_user.id)

@router.get("/{project_id}")
def read_project(project_id: int, db: Session = Depends(database.get_db)):
    project = get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}")
def modify_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    updated = update_project(db, project_id, project, current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found or not authorized")
    return updated

@router.delete("/{project_id}")
def remove_project(project_id: int, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    deleted = delete_project(db, project_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found or not authorized")
    return deleted
