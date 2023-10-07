from fastapi import APIRouter
from app.api.v1.users import users
from app.api.v1.courses import courses
from app.api.v1.categories import categories

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(courses.router, prefix="/courses", tags=["Courses"])
router.include_router(categories.router, prefix="/categories", tags=["Categories"])