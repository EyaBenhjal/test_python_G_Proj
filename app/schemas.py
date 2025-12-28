from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

    model_config = {
        "from_attributes": True  
    }
class ProjectCreate(BaseModel):
    title: str
    description: Optional[str]

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]
    assigned_to_id: Optional[int]
    status: Optional[str] = "todo"

class CommentCreate(BaseModel):
    content: str
class ProjectOut(BaseModel):
    id: int
    title: str
    description: Optional[str]

    model_config = {
        "from_attributes": True
    }
