from fastapi import FastAPI
from backend.routes.users import user
from backend.routes.courses import courses
from backend.routes.login import login
from backend.routes.login import router
from backend.routes.login_jwt import router as rout

app = FastAPI()
app.include_router(user)
app.include_router(courses)
app.include_router(router)
app.include_router(rout)



