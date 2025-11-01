from fastapi import APIRouter, status
from models.task import Task
from config.db import db
from utils.util_funcs import serialize_doc
from bson import ObjectId

router = APIRouter()

@router.get('/', tags=["Initial Routes"])
async def homepage():
    return "Nothing interesting here"

@router.get('/tasks', tags=["Tasks"])
async def get_tasks():
    result = await db["tasks"].find().to_list()
    tasks_list = [serialize_doc(task) for task in result]
    return tasks_list

@router.get('/tasks/{id}', tags=["Tasks"])
async def get_tasks(id: str):
    result = await db["tasks"].find_one()
    return serialize_doc(result)

@router.post('/tasks/create', status_code=status.HTTP_201_CREATED, tags=["Tasks"])
async def create_task(task: Task):
    result = await db["tasks"].insert_one(dict(task))
    return "Task Successfully Created"

@router.put('/tasks/update/{id}', tags=["Tasks"])
async def update_task(id: str, task: Task):
    result = await db["tasks"].find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(task)})
    return "Task Successfully Updated"

@router.delete('/tasks/delete/{id}', tags=["Tasks"])
async def delete_task(id: str):
    result = await db["tasks"].delete_one({"_id": ObjectId(id)})
    return "Task Successfully Deleted"
