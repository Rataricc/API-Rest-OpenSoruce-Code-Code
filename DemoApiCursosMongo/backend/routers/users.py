from fastapi import APIRouter, Depends, HTTPException, Response, status
#from backend.schemas.users import User, UserCreate
#from backend.models.users import UserDB, UserModel
from backend.db.connection import db_client
from backend.models.users import User
from backend.schemas.users import user_schema, GetUser

router = APIRouter(tags=["Users"], prefix="/users",
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user:User): 
    
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    user_dict = dict(user)
    #del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return User(**new_user)


@router.get("/")
async def get_users():
    return 'Hello Word'



def search_user(field: str, key): 
    try: 
        user = db_client.local.users.find_one({field:key})
        return User(**user_schema(user))
    except: 
        return {"Error": "No se ha encontrado el usuario"}
