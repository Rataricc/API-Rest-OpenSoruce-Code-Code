from pydantic import BaseModel

def user_schema(user) -> dict: 
    return { "id": str(user["_id"]), 
            "name": user["name"],
            "username": user["username"], 
            "email": user["email"], 
            "password": user["password"]
            }
    
class GetUser(BaseModel):
    id: str
    name: str
    username: str
    email: str
    password: str

  
"""
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str

class User(UserCreate):
    id: str
"""