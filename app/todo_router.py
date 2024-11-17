from fastapi import APIRouter


router = APIRouter(tags=["todos"])


@router.post("/todos/", status_code=201)
async def create_todos():
    return {"there are todos": "todos"}

@router.get("/todos/")
async def read_todos():
    todos = None
    return {"there are todos": todos}

@router.put("/todos/")
async def update_todos():
    upd_todos = None
    return{"there are updated todos": upd_todos}

@router.delete("/todos/")
async def delete_todos():
    dlt_todos = None
    return {"this todo were deleted:": dlt_todos}
#@router.post("/todos/", status_code=status.HTTP_201_CREATED)
#async def create_todos(todo: TodoCreated):
#    return {todo}