from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SchemaCourses(BaseModel): 
    title: str
    description: str
    instructor: str
    category: str
    url: str

class SchemaGetCourses(SchemaCourses): 
    id: int
    title: str
    description: str
    url: str
