from typing import Optional
from sqlmodel import SQLModel, Field
from enum import Enum

class LikeState(str, Enum): 
    NO_LIKE = "no_like"
    LIKE = "like"
    FAVORITO = "favorito"
    
    @classmethod
    def is_valid(cls, value):
        return any(value == item.value for item in cls)
    
    @classmethod
    def is_like(cls, value):
        return value in [cls.LIKE, cls.FAVORITO]

    @classmethod
    def is_favorito(cls, value):
        return value == cls.FAVORITO

    @classmethod
    def is_no_like(cls, value):
        return value == cls.NO_LIKE

#Model
class CourseBase(SQLModel):
    image: str = Field(index=True, title="Url Image", max_length=254)
    title: str = Field(index=True, max_length=254)
    description: str = Field(index=True, title="Description Course")
    url: str = Field(index=True, title="Url ubication course")
    likestate: LikeState
    

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
    likestate: Optional[LikeState] = None