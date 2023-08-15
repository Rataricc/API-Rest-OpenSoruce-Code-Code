from fastapi import APIRouter, Depends, HTTPException, Response
from backend.schemas.users import SchemaUser, SchemaGetUser

router = APIRouter(tags=["Users"])

@router.get("/")
async def get_users(): 
    return 'Hello Word'