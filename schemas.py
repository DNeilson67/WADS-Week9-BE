from typing import Union
from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, description="The updated title of the task")
    completed: Optional[bool] = Field(None, description="The updated completion status of the task")