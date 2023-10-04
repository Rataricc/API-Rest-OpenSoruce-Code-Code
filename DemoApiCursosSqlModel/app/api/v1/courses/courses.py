from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db.database import get_session
#Este todavia no existe el modelo o no esta agregado hay que agregarlo.
#from app.models.courses.courses import User, UserBase, UserCreate, UserRead, UserUpdate

router = APIRouter()