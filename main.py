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
