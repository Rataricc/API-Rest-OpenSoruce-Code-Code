from typing import Optional
from sqlmodel import SQLModel, Field

#Model
class CourseBase(SQLModel):
    image: str = Field(index=True, title="Url Image", max_length=254)
    title: str = Field(index=True, max_length=254)
    description: str = Field(index=True, title="Description Course")
    url: str = Field(index=True, title="Url ubication course")
    

#Hereda del modelo, schemas
class Courses(CourseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CourseCreate(CourseBase):
    pass

# schema para devolver los datos o verlos ---> response model
class CourseRead(CourseBase):
    id: int


class CourseUpdate(SQLModel):
    image: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None