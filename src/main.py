from fastapi import FastAPI

from src.routers import user
from src.db import database

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(user.router)
