from fastapi import FastAPI
from db import db
from utils import serialize_doc

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "FastAPI Test :)"}