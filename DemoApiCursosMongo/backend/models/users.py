from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str]
    name: str
    username: str
    email: str
    password: str