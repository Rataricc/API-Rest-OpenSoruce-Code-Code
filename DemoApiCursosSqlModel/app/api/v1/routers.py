from fastapi import APIRouter
from app.api.v1.users import users
from app.api.v1.courses import courses

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(courses.router, prefix="/courses", tags=["Courses"])