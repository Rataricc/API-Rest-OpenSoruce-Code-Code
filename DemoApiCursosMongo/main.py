from fastapi import FastAPI
from backend.routers.users import router

app = FastAPI()
app.include_router(router)