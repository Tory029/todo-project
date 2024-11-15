from pydantic import BaseModel
from datetime import datetime

class TodoMain(BaseModel):
    title: str
    content: str
    time: datetime


class TodoCreate(TodoMain):
    pass

class TodoUpdate(TodoMain):
    pass