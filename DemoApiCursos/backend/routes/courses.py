from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from backend.db.connection import Base, SessionLocal, engine
from backend.models.courses import Course 
from backend.schemas.schemacourses import SchemaCourses, SchemaGetCourses
from backend.db.connection import get_db
from backend.routes.login_jwt import auth_user

courses = APIRouter(tags=["Courses"], dependencies=[Depends(auth_user)])

@courses.post("/coursesCreate", response_model=SchemaCourses, status_code=201)
def create_courses(courses:SchemaCourses, db:Session =Depends(get_db)):     
    db_courses = Course(title=courses.title, instructor=courses.instructor, category=courses.category, description=courses.description, url=courses.url)
    try: 
        db.add(db_courses)
        db.commit()
        db.refresh(db_courses)
        return db_courses
    except IntegratyError: 
        db.rollback()
        raise HTTPException(status_code=400, detail="El usuario ya existe")


@courses.get("/get_courses", response_model=list[SchemaGetCourses])
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)): 
    courses_get = db.query(Course).offset(skip).limit(limit).all()
    return courses_get


@courses.get("/course/{course_id}", response_model=SchemaGetCourses, status_code=200)
def find_course(course_id: int, db: Session = Depends(get_db)): 
    find_course_id = db.query(Course).filter(Course.id == course_id).first()
    if find_course_id: 
        return find_course_id
    else: 
        raise HTTPException(status_code=404, detail="User not found")


@courses.delete("/courseDeleted/{course_id}", response_model=bool, status_code=200)
def delete_course(course_id: int, db: Session = Depends(get_db)): 
    is_delete = db.query(Course).filter(Course.id == course_id).first()
    if is_delete: 
        db.delete(is_delete)
        db.commit()
        return True
    else: 
        raise HTTPException(status_code=404, detail="User not found")


@courses.put("/course_update/{course_id}", response_model=SchemaCourses, status_code=201)
def update_course(course_id: int, updated_course: SchemaCourses, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    db_course.title = updated_course.title
    db_course.description = updated_course.description
    db_course.instructor = update_course.instructor
    db_course.category = update_course.category
    db_course.url = updated_course.url
    db.commit()
    db.refresh(db_course)

    return db_course