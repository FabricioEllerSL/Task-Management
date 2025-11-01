from fastapi import FastAPI
from config.db import db
from utils.util_funcs import serialize_doc
from routes.routes import router

app = FastAPI()

app.include_router(router)