from fastapi import FastAPI
from backend.routes.users import user
from backend.routes.courses import courses
from backend.routes.login import login

app = FastAPI()
app.include_router(user)
app.include_router(courses)
app.include_router(login)

