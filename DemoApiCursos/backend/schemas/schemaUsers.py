from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SchemaUser(BaseModel):
    name: str
    username: str
    email: str
    password: str
    datetime: datetime

class SchemaGetUser(SchemaUser):
    id : int
    name: str
    username: str
    email: str
    datetime: datetime
    

"""
class SchemaUserCreate(BaseModel):
    name: str
    email: str
    password: str


class SchemaUserBasic(BaseModel):
    name: str
    email: str
"""