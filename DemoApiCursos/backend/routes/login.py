# Login basico

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Response
from backend.db.connection import Base, SessionLocal, engine
from backend.db.connection import get_db
from backend.schemas.schemaUsers import SchemaGetUser, SchemaUser
from backend.models.users import User

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter(tags=["Login"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/login")
async def login_view(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


#--------------------------------------------------------------------------------------
    # todavia no funciona del todo seguir viendo. Pues no funciono de esta manera.
def get_user(username: str, db:Session): 
    user = db.query(User).filter(User.username == username).options(load_only("id", "name", "username", "email")).first()
    if user is None: 
        return None
    return user
# Funciono abajo de esta funcion ↓↓↓↓


def get_user_by_username(username: str, db:Session): 
    user = db.query(User).filter(User.username == username).first()
    if user is None: 
        return None
    return user

async def current_user(token: str = Depends(oauth2_scheme), db:Session = Depends(get_db)): 
    user = get_user_by_username(token, db)
    if not user: 
        raise HTTPException(status_code=401, detail="Credenciales de autenticacion invalidas", headers={"WWW-Authenticate":"Baerer"})
    return user

# De prueba, para autenticacion
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)): 
    user_db = get_user_by_username(form.username, db)
    if not user_db: 
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    
    user = get_user_by_username(form.username, db)
    if not form.password == user.password: 
        raise HTTPException(status_code=400, detail="La contraseña es incorrecta")
    
    return {"access_token": user.username, "token_type":"bearer"}


@router.get("/users/me")
async def me(user: SchemaGetUser = Depends(current_user)): 
    return  {"id":user.id, "name": user.name, "username":user.username, "email": user.email}

#------------------------------------------------------------------------------------------------------

#Ver esto a detalle, crear las otras funcionalidades de token para validar, no esta terminado... 
#Pero esta andando bien, me tira: "detail": "Not authenticated"
@router.get("/login/me", response_model=list[SchemaGetUser])
async def get_user_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)): 
    users_get = db.query(User).offset(skip).limit(limit).all()
    return users_get