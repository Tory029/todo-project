import uvicorn

from fastapi import FastAPI
from todo_router import router


app = FastAPI(title='Home')


@app.get("/", status_code=200)
async def home():
    return {"its": "home page"}


app.include_router(router=router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app', 
        reload=True,
        host='localhost',
        port=5432,
        )