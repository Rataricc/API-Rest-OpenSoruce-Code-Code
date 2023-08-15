from pydantic import BaseModel

class SchemaUser(BaseModel):
    name: str
    username: str
    email: str
    password: str

class SchemaGetUser(SchemaUser):
    id : int
    name: str
    username: str
    email: str
   