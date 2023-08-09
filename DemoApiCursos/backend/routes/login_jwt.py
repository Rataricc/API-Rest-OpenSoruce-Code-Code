# Login jwt (Json Web Token)

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Response
from backend.db.connection import Base, SessionLocal, engine
from backend.db.connection import get_db
from backend.schemas.schemaUsers import SchemaGetUser, SchemaUser
from backend.models.users import User
from datetime import datetime, timedelta


#datetime ---> para la fecha del sistema. 
#timedelta ----> para trabajar con calculos de fecha.

from backend.routes.login import get_user_by_username

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
                           
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1 #minutos
SECRET = "68a5df4174ac0c803f6c9125113017c3504693c24acbfbba914fcc13dcf795bd"

router = APIRouter(tags=["Login_jwt"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

crypt = CryptContext(schemes=["bcrypt"])


# En resumen, la función auth_user se encarga de autenticar y verificar la validez del token JWT 
# proporcionado, decodificar el token para obtener el nombre de usuario, y buscar al usuario correspondiente 
# en la base de datos utilizando el nombre de usuario.
async def auth_user(token: str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    exception = HTTPException(status_code=401, detail="Credenciales de autenticacion invalidas", headers={"WWW-Authenticate":"Baerer"})
    try: 
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None: 
            raise exception
    except JWTError:  
        raise exception
    return get_user_by_username(username, db)

# Busca usuario por username en la base de datos.
def get_user_by_username(username: str, db:Session): 
    user = db.query(User).filter(User.username == username).first()
    if user is None: 
        return None
    return user

# se utiliza para verificar la validez de un token de autenticación, buscar al usuario 
# correspondiente en la base de datos y proporcionar ese usuario a la función principal 
# que depende de esta dependencia.
"""
async def current_user(token: str = Depends(oauth2_scheme), db:Session = Depends(get_db)): 
    user = get_user_by_username(token, db)
    if not user: 
        raise HTTPException(status_code=401, detail="Credenciales de autenticacion invalidas", headers={"WWW-Authenticate":"Baerer"})
    return user
"""


@router.post("/login_jwt")
async def login(form: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)): 
    user_db = get_user_by_username(form.username, db)
    if not user_db: 
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    
    user = get_user_by_username(form.username, db)
    
    if not crypt.verify(form.password, user.password): 
        raise HTTPException(status_code=400, detail="La contraseña es incorrecta")
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = {"sub":user.username, "exp":expire}
    
    token = jwt.encode(access_token, SECRET, algorithm=ALGORITHM)
    
    return {"access_token": token, "token_type":"bearer"}


@router.get("/users/me/jwt")
async def me(user: SchemaGetUser = Depends(auth_user)): 
    return  {"id":user.id, "name": user.name, "username":user.username, "email": user.email}


#--------------------------------------------------------------------------------------------------

"""
async def auth_user(token: str = Depends(oauth2_scheme), db:Session = Depends(get_db)): 
    
    exception = HTTPException(status_code=401, detail="Credenciales de autenticacion invalidas", headers={"WWW-Authenticate":"Baerer"})

    
    try: 
        username = jwt.decode(token, SECRET, algorithm=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:  
        raise exception
    
    return {"username":username}
    
        
async def current_user(user: User = Depends(oauth2_scheme), db:Session = Depends(get_db)): 
    user = get_user_by_username(token, db)
    if not user: 
        raise HTTPException(status_code=401, detail="Credenciales de autenticacion invalidas", headers={"WWW-Authenticate":"Baerer"})
    return user



@router.post("/login_jwt")
async def login(form: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)): 
    user_db = get_user_by_username(form.username, db)
    if not user_db: 
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    
    
    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status_code=400, detail="La contraseña es incorrecta")
    
   
    #expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # entonces: ¿cuando va a expirar? 
    # Justo el tiempo que es ahora más (+) un minuto que se guarda en la variable ACCESS_TOKEN_EXPIRE_MINUTES
    access_token = {"sub": user_db.username, 
                    "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
    
    token = jwt.encode(access_token, SECRET,algorithm=ALGORITHM)
    
    return {"access_token":token, "token_type":"bearer"}


@router.get("/users/me")
async def me(user: SchemaGetUser = Depends(current_user)): 
    return  {"id":user.id, "name": user.name, "username":user.username, "email": user.email}
"""