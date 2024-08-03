
from fastapi import APIRouter, HTTPException, Form, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.register_buyer_seller import User
from pydantic import BaseModel

class UserCreate(BaseModel):
    full_name: str
    user_id: str
    password: str
    buyer_or_seller: str  # Add role field

class UserResponse(BaseModel):
    full_name: str
    user_id: str
    buyer_or_seller: str  # Add role field

    class Config:
        orm_mode = True



router = APIRouter()

@router.post("/register/", response_model=UserResponse)
async def create_user(
    full_name: str = Form(...),
    user_id: str = Form(...),
    password: str = Form(...),
    buyer_or_seller: str = Form(...),  # Add role field
    db: Session = Depends(get_db)
):
     # Check if user ID is already registered
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User ID already registered")

    new_user = User(
        full_name=full_name,
        user_id=user_id,
        password=password,
        buyer_or_seller=buyer_or_seller  # Set role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login/", response_model=UserResponse)
async def login_user(
    user_id: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    
    
    user = db.query(User).filter(User.user_id == user_id).first()
    
    # Check if user exists and password matches
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid user ID or password")
    
    return user
