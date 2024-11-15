from fastapi import APIRouter
from db import get_todos

router = APIRouter()


@router.get("/todos/")
async def read_todos():
    todos = get_todos()
    return {"there are todos": todos}