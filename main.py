from fastapi import FastAPI
import uvicorn

from db.base import database
from endpoints import user_list_get, user_post, user_put, auth, user_patch, user_delete

app = FastAPI()
app.include_router(user_post.router, tags=["users"])
app.include_router(user_list_get.router, tags=["users"])
app.include_router(user_put.router, tags=["users"])
app.include_router(auth.router, tags=["users"])
app.include_router(user_patch.router, tags=["users"])
app.include_router(user_delete.router, tags=["users"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
