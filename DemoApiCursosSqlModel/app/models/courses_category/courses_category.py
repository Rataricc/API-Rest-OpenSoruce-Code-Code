from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
#from app.models.courses.course import Courses
#from app.models.categories.category import Categories

#Model
class CoursesCategoryBase(SQLModel):
    course_id: Optional[int] = Field(default=None, foreign_key="courses.id")
    category_id: Optional[int] = Field(default=None, foreign_key="categories.id") 
    
    #course: Courses = Relationship(back_populates="categories")
    #category: Categories = Relationship(back_populates="courses")
    
    
#Hereda del modelo, schemas
class CoursesCategory(CoursesCategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    

class CoursesCategoryCreate(CoursesCategoryBase):
    pass

# schema para devolver los datos o verlos ---> response model
class CoursesCategoryRead(CoursesCategoryBase):
    id: int


class CoursesCategoryUpdate(SQLModel):
   pass