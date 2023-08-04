from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Response
from backend.db.connection import Base, SessionLocal, engine
from backend.db.connection import get_db

from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

login = APIRouter(tags=["Login"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@login.get("/login")
async def login_view(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}