from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from model import Task
from schema import task_schema
from session import create_get_session, get_database_session

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Server is up and runnning!"}


@app.get("/task", response_model=List[task_schema], status_code=200)
async def read_tasks(db: Session = Depends(create_get_session)):
    tasks = db.query(Task).all()
    return tasks


@app.post("/task", response_model=task_schema, status_code=201)
async def create_task(task: task_schema, db: Session = Depends(create_get_session)):
    new_task = Task(
        task_name=task.task_name,
        task_des=task.task_des,
        created_by=task.created_by,
        date_created=task.date_created,
    )
    db.add(new_task)
    db.commit()

    return new_task
