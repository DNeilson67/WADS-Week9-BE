from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas


def get_task_by_id(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if task:
        return task
    else: raise HTTPException(status_code=404, detail="Task not found")

def get_task_by_title(db: Session, title: str):
    task = db.query(models.Task).filter(models.Task.title == title).first()
    if task:
        return task
    else: raise HTTPException(status_code=404, detail="Task not found")

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    if tasks:
        return tasks
    else: raise HTTPException(status_code=404, detail="Task is empty")

def get_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        return user
    else: raise HTTPException(status_code=404, detail="User not found")

def get_user_by_email(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        return user
    return

def get_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(models.User).offset(skip).limit(limit).all()
    if users:
        return users
    else: raise HTTPException(status_code=404, detail="User is empty")

def create_task(db: Session, task: schemas.Task):
    db_task = models.Task(title = task.title, completed = task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def create_user(db: Session, user: schemas.User):
    fake_hashed_password = user.password + "notreallyhashed"
    user = models.User(username = user.username, email=user.email, password=fake_hashed_password)
    db.add(user) 
    db.commit()
    db.refresh(user)
    return user

def delete_task_by_id(db: Session, id: int):
    task = get_task_by_id(db, id)
    if task:
        db.delete(task)
        db.commit()
        return {"message":"Task Deleted Successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

def delete_task_by_title(db: Session, title: str):
    task = get_task_by_title(db, title)
    if task:
        db.delete(task)
        db.commit()
        return {"message":"Task Deleted Successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")


def delete_user_by_email(db: Session, email: str):
    user = get_user_by_email(db, email)
    if user:
        db.delete(user)
        db.commit()
        return {"message":"User Deleted Successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")  
    
def delete_all_tasks(db: Session):
    if db.query(models.Task).delete():
        db.commit()
        return {"message":"Task Deleted Successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task is empty") 

def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    # Fetch the task from the database
    db_task = get_task_by_id(db, task_id)
    
    # Check if the task exists
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update the task attributes based on the provided data
    for field, value in task_update.model_dump().items():
        setattr(db_task, field, value)
    
    # Commit the changes to the database
    db.commit()
    
    # Return the updated task
    return {"message" : "Task Updated Successfully"}
    

# def create_task_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item