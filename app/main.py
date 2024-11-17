import uvicorn
import typer
import asyncio

from fastapi import FastAPI
from todo_router import router
#from db import init_models


app = FastAPI()
app.include_router(router)
        
#cli = typer.Typer()

#@cli.command()
#def db_init_models():
#    asyncio.run(init_models())
 #   print("Done")


if __name__ == '__main__':
    uvicorn.run(
        'main:app', 
        reload=True,
        host='localhost',
        port=5432,
        )
    #cli()