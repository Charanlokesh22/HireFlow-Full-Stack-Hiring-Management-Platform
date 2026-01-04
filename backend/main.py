from fastapi import FastAPI
from routes import jobs, users
from database import init_db

app = FastAPI(title="HireFlow API")

@app.on_event("startup")
async def start():
    await init_db()

app.include_router(users.router, prefix="/users")
app.include_router(jobs.router, prefix="/jobs")
