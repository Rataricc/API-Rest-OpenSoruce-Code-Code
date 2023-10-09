from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from typing import List
from app.models.courses.course import Courses

#Model
class UserBase(SQLModel):
    full_name: str = Field(index=True, title="Pedro Pica Piedra", max_length=254)
    username: str = Field(index=True, max_length=25)
    email: str = Field(index=True, title="Email address", max_length=45)
    password: str = Field(index=True, title="Password", max_length=45)
    
    #course_id: int = Field(default=None, foreign_key="courses.id")
    #course: List[Courses] = Relationship(back_populates="user")
    

#Hereda del modelo, schemas
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    courses: List["Courses"] = Relationship(back_populates="user")   

class UserCreate(UserBase):
    pass

# schema para devolver los datos o verlos ---> response model
class UserRead(UserBase):
    id: int


class UserUpdate(SQLModel):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
