from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Response
from backend.db.connection import Base, SessionLocal, engine
from backend.models.users import User 
from backend.schemas.schemaUsers import SchemaUser, SchemaGetUser
from backend.db.connection import get_db
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from backend.routes.login_jwt import auth_user

import datetime

# user = APIRouter(tags=["Users"], dependencies=[Depends(auth_user)])
user = APIRouter(tags=["Users"])


@user.post("/user", response_model=SchemaUser, status_code=201)
def create_user(user:SchemaUser, db:Session =Depends(get_db)):     
    db_user = User(name=user.name, username=user.username, email=user.email, password=user.password, datetime=user.datetime)
    try: 
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegratyError: 
        db.rollback()
        raise HTTPException(status_code=400, detail="El usuario ya existe")


@user.get("/users", response_model=list[SchemaGetUser], dependencies=[Depends(auth_user)])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)): 
    users_get = db.query(User).offset(skip).limit(limit).all()
    return users_get



@user.get("/user/{user_id}", response_model=SchemaUser, dependencies=[Depends(auth_user)])
def find_user(user_id: int, db: Session = Depends(get_db)): 
    find_user_id = db.query(User).filter(User.id == user_id).first()
    if find_user: 
        return find_user_id
    else: 
        raise HTTPException(status_code=404, detail="User not found")


@user.delete("/user/{user_id}", response_model=bool, dependencies=[Depends(auth_user)])
def delete_user(user_id: int, db: Session = Depends(get_db)): 
    is_delete = db.query(User).filter(User.id == user_id).first()
    if is_delete: 
        db.delete(is_delete)
        db.commit()
        return True
    else: 
        raise HTTPException(status_code=404, detail="User not found")


@user.put("/user/{user_id}", response_model=SchemaUser, dependencies=[Depends(auth_user)])
def update_user(user_id: int, updated_user: SchemaUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = updated_user.name
    db_user.username = update_user.username
    db_user.email = updated_user.email
    db_user.password = updated_user.password
    db.commit()
    db.refresh(db_user)

    return db_user