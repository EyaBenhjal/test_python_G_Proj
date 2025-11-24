from sqlalchemy.orm import Session
from .. import models, schemas

def get_comments_by_task(db: Session, task_id: int):
    return db.query(models.Comment).filter(models.Comment.task_id == task_id).all()

def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def create_comment(db: Session, task_id: int, comment: schemas.CommentCreate, owner_id: int):
    db_comment = models.Comment(
        content=comment.content,
        task_id=task_id,
        owner_id=owner_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment(db: Session, comment_id: int, comment: schemas.CommentCreate, owner_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id, models.Comment.owner_id == owner_id).first()
    if not db_comment:
        return None
    db_comment.content = comment.content
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int, owner_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id, models.Comment.owner_id == owner_id).first()
    if not db_comment:
        return None
    db.delete(db_comment)
    db.commit()
    return {"ok": True}
