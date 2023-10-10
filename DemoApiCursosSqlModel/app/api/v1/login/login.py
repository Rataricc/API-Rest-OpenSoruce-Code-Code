# Login jwt (Json Web Token)
from sqlmodel import create_engine, Session, select
from fastapi import APIRouter, Depends, HTTPException, Response
from app.db.database import get_session
from app.models.users.user import User, UserBase, UserCreate, UserRead
from datetime import datetime, timedelta
# datetime ---> para la fecha del sistema.
# timedelta ----> para trabajar con calculos de fecha.
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from dotenv import load_dotenv
import os


ALGORITHM = os.getenv("ALGORITHM")
SECRET = os.getenv("SECRET")
ACCESS_TOKEN_EXPIRE_MINUTES = 1  # minutos

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

crypt = CryptContext(schemes=["bcrypt"])

# Busca usuario por username en la base de datos.
def get_user_by_username(username: str, session: Session):
    user = session.exec(select(User).where(User.username == username)).first()
    if user is None:
        return None
    return user


# En resumen, la función auth_user se encarga de autenticar y verificar la validez del token JWT
# proporcionado, decodificar el token para obtener el nombre de usuario, y buscar al usuario correspondiente
# en la base de datos utilizando el nombre de usuario.
async def auth_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    exception = HTTPException(status_code=401, detail="Credenciales de autenticacion invalidas", headers={
                              "WWW-Authenticate": "Baerer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    return get_user_by_username(username, session)


@router.post("/login_jwt")
async def login(form: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user_db = get_user_by_username(form.username, session)
    if not user_db:
        raise HTTPException(
            status_code=400, detail="El usuario no es correcto")
    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(
            status_code=400, detail="La contraseña es incorrecta")
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = {"sub": user_db.username, "exp": expire}
    token = jwt.encode(access_token, SECRET, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/users/me/jwt")
async def me(user: UserRead = Depends(auth_user)):
    return {"id": user.id, "full_name": user.full_name, "username": user.username, "email": user.email}