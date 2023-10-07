from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from typing import List
#from app.models.courses_category.courses_category import CoursesCategory

#Model
class CategoryeBase(SQLModel):
    name: str = Field(index=True, title="Category name ", max_length=254)
    
    course_id: int = Field(default=None, foreign_key="coursescategory.id")
    #courses: List[CoursesCategory] = Relationship(back_populates="categories")
    
    
#Hereda del modelo, schemas
class Categories(CategoryeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CategoriesCreate(CategoryeBase):
    pass

# schema para devolver los datos o verlos ---> response model
class CategoriesRead(CategoryeBase):
    id: int


class CategoryUpdate(SQLModel):
    name: Optional[str] = None
   