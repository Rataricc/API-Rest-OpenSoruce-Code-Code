from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.users.user import User, UserBase, UserCreate, UserRead, UserUpdate
from app.api.v1.login.login import auth_user

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user(*, session: Session = Depends(get_session), data: UserCreate):
    with session: 
        new_user = User.from_orm(data)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user


@router.get("/", response_model=list[UserRead], dependencies=[Depends(auth_user)])
async def get_users(*, session: Session = Depends(get_session)): 
    with session:
        users = session.exec(select(User)).all()
        return users


@router.get("/limit", response_model=list[UserRead], dependencies=[Depends(auth_user)])
async def get_users_limit(*, offset: int = 0, limit: int = 10, session: Session = Depends(get_session)): 
    with session:
        users = session.exec(select(User).offset(offset).limit(limit)).all()
        return users   


@router.get("/find/{id}", response_model=UserRead)
async def find_user(id: int, session: Session = Depends(get_session)): 
    with session:
        users = session.exec(select(User).where(User.id == id)).first()
        return users    

    
@router.get("/find/{username}", response_model=UserRead)
async def find_user_username(username: str, session: Session = Depends(get_session)): 
    with session:
        users = session.exec(select(User).where(User.username == username)).first()
        return users  
    

@router.put("/{id}", response_model=UserRead, dependencies=[Depends(auth_user)])
async def update_user_by_id(id: int, updated_user: UserUpdate, session: Session = Depends(get_session)):
    with session:
        user = session.get(User, id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Actualiza los campos según los valores proporcionados
        user.full_name = updated_user.full_name
        user.username = updated_user.username
        user.email = updated_user.email
        user.password = updated_user.password
    
        session.add(user)
        session.commit()
        session.refresh(user)
        
        return user


@router.delete("/{id}", dependencies=[Depends(auth_user)])
async def delete_user_by_id(id: int,  session: Session = Depends(get_session)):
    with session:
        user = session.get(User, id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(user)
        session.commit()

        return {"message": f"User with ID {id} deleted successfully"}    