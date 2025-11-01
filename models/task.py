from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class Priority(Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(BaseModel):
    name: str
    description: str
    due_date: datetime
    priority: Priority = Field(default=Priority.medium)
    done: bool