from fastapi import APIRouter, Depends, HTTPException, Response, status
#from backend.schemas.users import User, UserCreate
#from backend.models.users import UserDB, UserModel
from backend.db.connection import db_client
from backend.models.users import User
from backend.schemas.users import user_schema, GetUser, users_get

router = APIRouter(tags=["Users"], prefix="/users",
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


# Solamente de prueba.
@router.post("/create_user", response_model= User, status_code=status.HTTP_201_CREATED)
async def user_create(user: User): 
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    elif type(search_user("username", user.username)) == User: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe, elija otro nombre de usuario")
    new_user = dict(user)
    del new_user["id"]
    result = db_client.local.user.insert_one(new_user).inserted_id
    user = db_client.local.user.find_one({"_id":result})
    return user_schema(user)


@router.get("/find_user", response_model=list[User],status_code=status.HTTP_200_OK)
async def find_user(): 
    return users_get(db_client.local.user.find())


"""
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user:User): 
    # Verificar si el usuario ya existe
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")


    user_dict = user.dict(exclude_unset=True)
    # Eliminar el campo 'id' del objeto user
    #user_dict.pop("id", None)
    #del user_dict["id"]
     
    # Insertar el usuario en la base de datos
    result = db_client.local.users.insert_one(user_dict)
    
    # Obtener el ID generado por MongoDB
    new_user_id = str(result.inserted_id)
    
    # Crear el objeto de respuesta con el ID y otros datos
    new_user_response = user_dict.copy()
    new_user_response["_id"] = new_user_id
    

    return new_user_response

"""

def search_user(field: str, key): 
    try: 
        user = db_client.local.user.find_one({field:key})
        return User(**user_schema(user))
    except: 
        return {"Error": "No se ha encontrado el usuario"}
