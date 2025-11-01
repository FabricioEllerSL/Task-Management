from fastapi import APIRouter
from models.task import Task
from config.db import db
from utils.util_funcs import serialize_doc
from bson import ObjectId


router = APIRouter()


@router.get('/')
async def homepage():
    return "you are in the first route"

