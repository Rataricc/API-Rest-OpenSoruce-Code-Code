from fastapi import APIRouter
from . import courses
from . import users 

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(courses.router, prefix="/courses", tags=["Courses"])