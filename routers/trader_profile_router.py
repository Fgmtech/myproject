
from fastapi import FastAPI, HTTPException, Form, UploadFile, File, Depends, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from sqlalchemy import create_engine, Column, String, Integer, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config.config import settings
from database.db import Base, get_db
from models.trader_profile import Trader


router = APIRouter()

class TraderCreate(BaseModel):
    trader_id: str
    name: str
    username: str
    phone_number: Optional[str] = None
    social_media_links: Optional[str] = None
    university: str
    department: str
    year_of_study: str
    business_name: str
    business_description: Optional[str] = None
    category: str
    location: Optional[str] = None
    product_listings: Optional[str] = None
    pricing: Optional[str] = None
    availability: Optional[str] = None
    verification_status: Optional[str] = "unverified"
    id_verification: Optional[str] = "unverified"
    payment_methods: Optional[str] = None
    response_time: Optional[str] = None
    warranty_information: Optional[str] = None
    special_offers: Optional[str] = None
    portfolio: Optional[str] = None
    
    
    

@router.post("/traders/", response_model=TraderCreate)
async def create_trader(
    trader_id: str = Form(...),
    name: str = Form(...),
    username: str = Form(...),
    phone_number: Optional[str] = Form(None),
    social_media_links: Optional[str] = Form(None),
    university: str = Form(...),
    department: str = Form(...),
    year_of_study: str = Form(...),
    business_name: str = Form(...),
    business_description: Optional[str] = Form(None),
    category: str = Form(...),
    location: Optional[str] = Form(None),
    product_listings: Optional[str] = Form(None),
    pricing: Optional[str] = Form(None),
    availability: Optional[str] = Form(None),
    verification_status: Optional[str] = Form("unverified"),
    id_verification: Optional[str] = Form("unverified"),
    payment_methods: Optional[str] = Form(None),
    response_time: Optional[str] = Form(None),
    special_offers: Optional[str] = Form(None),
    portfolio: Optional[str] = Form(None),
    profile_picture: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
 
):
    # Save profile picture if provided
    if profile_picture:
        picture_path = f"images/{trader_id}_{profile_picture.filename}"
        with open(picture_path, "wb") as image_file:
            content = await profile_picture.read()
            image_file.write(content)
    else:
        picture_path = None

    trader = Trader(
        trader_id=trader_id,
        name=name,
        username=username,
        phone_number=phone_number,
        social_media_links=social_media_links,
        university=university,
        department=department,
        year_of_study=year_of_study,
        business_name=business_name,
        business_description=business_description,
        category=category,
        location=location,
        product_listings=product_listings,
        pricing=pricing,
        availability=availability,
        verification_status=verification_status,
        id_verification=id_verification,
        payment_methods=payment_methods,
        response_time=response_time,
        special_offers=special_offers,
        portfolio=portfolio,
        profile_picture=picture_path
    )

    db.add(trader)
    db.commit()
    db.refresh(trader)

    return trader

@router.get("/traders/{trader_id}", response_model=TraderCreate)
async def get_trader(trader_id: str, db: Session = Depends(get_db)):
    trader = db.query(Trader).filter(Trader.trader_id == trader_id).first()
    if not trader:
        raise HTTPException(status_code=404, detail="Trader not found")
    return trader

