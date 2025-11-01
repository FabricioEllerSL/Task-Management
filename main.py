from fastapi import FastAPI
from config.db import db
from utils.util_funcs import serialize_doc

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "FastAPI Test :)"}