from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index= True)
    email = Column(String[50], unique=True)
    password = Column(String[50])
    username = Column(String[50])


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index= True)
    title = Column(String[50])
    completed = Column(Boolean)
    # userID = Column(Integer, ForeignKey("users.id"))

    

