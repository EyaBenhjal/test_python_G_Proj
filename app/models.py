from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    # projets possédés par l'utilisateur
    projects_owned = relationship(
        "Project",
        back_populates="owner"
    )

    # tâches assignées / créées
    tasks_assigned = relationship(
        "Task",
        foreign_keys="[Task.assigned_to_id]",
        back_populates="assigned_to_user"
    )
    tasks_owned = relationship(
        "Task",
        foreign_keys="[Task.owner_id]",
        back_populates="owner"
    )

    # commentaires postés par l'utilisateur (one-to-many)
    comments = relationship(
        "Comment",
        back_populates="owner",
        foreign_keys="[Comment.owner_id]",
        cascade="all, delete-orphan"
    )

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="projects_owned")

    tasks = relationship("Task", back_populates="project")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="todo")

    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="tasks")

    assigned_to_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    assigned_to_user = relationship(
        "User",
        foreign_keys=[assigned_to_id],
        back_populates="tasks_assigned"
    )

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship(
        "User",
        foreign_keys=[owner_id],
        back_populates="tasks_owned"
    )

    # one-to-many: une tâche --> plusieurs commentaires
    comments = relationship("Comment", back_populates="task", cascade="all, delete-orphan")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    task_id = Column(Integer, ForeignKey("tasks.id"))
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)   # user who posted

    # relations explicites
    task = relationship("Task", back_populates="comments")
    owner = relationship("User", foreign_keys=[owner_id], back_populates="comments")
