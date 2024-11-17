from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    content: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int

