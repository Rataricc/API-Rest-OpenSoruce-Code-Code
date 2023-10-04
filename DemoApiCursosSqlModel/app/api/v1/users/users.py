from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db.database import get_session

from app.models.users.user import User, UserBase, UserCreate, UserRead, UserUpdate

router = APIRouter()


@router.post("/", response_model=UserRead)
async def create_user(*, session: Session = Depends(get_session), data: UserCreate):

    with session: 
        new_user = User.from_orm(data)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user


@router.get("/", response_model=list[UserRead])
async def get_users(*, session: Session = Depends(get_session)): 
    
    with session:
        users = session.exec(select(User)).all()
        return users
   