
from fastapi import APIRouter, HTTPException, Form, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.register_buyer_seller import User


from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    ID_number: str
    password: str
    role: str  # Add role field

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    ID_number: str
    role: str  # Add role field

    class Config:
        orm_mode = True



router = APIRouter()

@router.post("/register/", response_model=UserResponse)
async def create_user(
    first_name: str = Form(...),
    last_name: str = Form(...),
    ID_number: str = Form(...),
    password: str = Form(...),
    role: str = Form(...),  # Add role field
    db: Session = Depends(get_db)
):
    if db.query(User).filter(User_ID_number == ID_number).first():
        raise HTTPException(status_code=400, detail="ID number already registered")

    new_user = User(
        first_name=first_name,
        last_name=last_name,
        ID_number=ID_number,
        password=password,
        role=role  # Set role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login/", response_model=UserResponse)
async def login_user(
    ID_number: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User_ID_number == ID_number).first()
    if not user or user_password != password:
        raise HTTPException(status_code=401, detail="Invalid ID number or password")
    return user
