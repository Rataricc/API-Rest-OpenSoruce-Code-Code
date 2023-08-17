from pydantic import BaseModel
from typing import Optional



class CretaeUser(BaseModel):
    #id: Optional[str]
    name: str
    username: str
    email: str
    password: str

class User(CretaeUser):
    id: Optional[str]
    
    