from sqlalchemy.orm import Session
from .. import models, schemas

def get_tasks_by_project(db: Session, project_id: int):
    return db.query(models.Task).filter(models.Task.project_id == project_id).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, project_id: int, task: schemas.TaskCreate, owner_id: int):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        project_id=project_id,
        assigned_to_id=task.assigned_to_id,   
        owner_id=owner_id,                    
        status=task.status or "todo",
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: schemas.TaskCreate):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return None
    db_task.title = task.title
    db_task.description = task.description
    db_task.status = task.status or db_task.status
    db_task.assigned_to_id = task.assigned_to_id
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, owner_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == owner_id).first()
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return {"ok": True}
