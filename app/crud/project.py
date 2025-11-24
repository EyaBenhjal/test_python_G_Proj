from sqlalchemy.orm import Session
from .. import models, schemas

def get_all_projects(db: Session):
    return db.query(models.Project).all()

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def create_project(db: Session, project: schemas.ProjectCreate, owner_id: int):
    db_project = models.Project(
        title=project.title,
        description=project.description,
        owner_id=owner_id
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: int, project: schemas.ProjectCreate, owner_id: int):
    db_project = db.query(models.Project).filter(models.Project.id == project_id, models.Project.owner_id == owner_id).first()
    if not db_project:
        return None
    db_project.title = project.title
    db_project.description = project.description
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int, owner_id: int):
    db_project = db.query(models.Project).filter(models.Project.id == project_id, models.Project.owner_id == owner_id).first()
    if not db_project:
        return None
    db.delete(db_project)
    db.commit()
    return {"ok": True}
