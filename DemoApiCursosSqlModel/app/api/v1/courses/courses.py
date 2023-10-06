from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db.database import get_session
from app.models.courses.course import Courses, CourseBase, CourseCreate, CourseRead, CourseUpdate

router = APIRouter()

@router.post("/", response_model=CourseRead)
async def create_course(*, session: Session = Depends(get_session), data: CourseCreate):

    with session: 
        new_course = Courses.from_orm(data)
        session.add(new_course)
        session.commit()
        session.refresh(new_course)
        return new_course


@router.get("/", response_model=list[CourseRead])
async def get_courses(*, session: Session = Depends(get_session)): 
    
    with session:
        courses = session.exec(select(Courses)).all()
        return courses


@router.get("/limit", response_model=list[CourseRead])
async def get_courses_limit(*, offset: int = 0, limit: int = 10, session: Session = Depends(get_session)): 
    
    with session:
        courses = session.exec(select(Courses).offset(offset).limit(limit)).all()
        return courses   


@router.get("/find/{id}", response_model=CourseRead)
async def find_course(id: int, session: Session = Depends(get_session)): 
    
    with session:
        courses = session.exec(select(Courses).where(Courses.id == id)).first()
        return courses    

    
@router.get("/find/{title}", response_model=CourseRead)
async def find_course_title(title: str, session: Session = Depends(get_session)): 
    
    with session:
        courses = session.exec(select(Courses).where(Courses.title == title)).first()
        return courses  
    

@router.put("/{id}", response_model=CourseRead)
async def update_course_by_id(id: int, updated_course: CourseUpdate, session: Session = Depends(get_session)):
   
    with session:
        course = session.get(Courses, id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        # Actualiza los campos según los valores proporcionados
        course.image = updated_course.image
        course.title = updated_course.title
        course.description = updated_course.description
        course.url = updated_course.url
    
        session.add(course)
        session.commit()
        session.refresh(course)
        
        return course


@router.delete("/{id}")
async def delete_course_by_id(id: int,  session: Session = Depends(get_session)):
   
    with session:
        course = session.get(Courses, id)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        session.delete(course)
        session.commit()
        
        return {"message": f"Course with ID {id} deleted successfully"}    