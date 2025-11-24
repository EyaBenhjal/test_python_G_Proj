from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, database
from app.crud.comment import get_comments_by_task, get_comment, create_comment, update_comment, delete_comment
from app.routers.auth import get_current_user

router = APIRouter()

@router.get("/tasks/{task_id}/comments")
def read_comments(task_id: int, db: Session = Depends(database.get_db)):
    return get_comments_by_task(db, task_id)

@router.post("/tasks/{task_id}/comments")
def create_new_comment(task_id: int, comment: schemas.CommentCreate, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    return create_comment(db, task_id, comment, current_user.id)

@router.get("/{comment_id}")
def read_comment(comment_id: int, db: Session = Depends(database.get_db)):
    return get_comment(db, comment_id)

@router.put("/{comment_id}")
def update_existing_comment(comment_id: int, comment: schemas.CommentCreate, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    return update_comment(db, comment_id, comment, current_user.id)

@router.delete("/{comment_id}")
def delete_existing_comment(comment_id: int, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    return delete_comment(db, comment_id, current_user.id)
