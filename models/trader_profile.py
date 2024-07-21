
from fastapi import FastAPI, HTTPException, Form, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from sqlalchemy import create_engine, Column, String, Integer, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config.config import settings
from database.db import Base, get_db




class Trader(Base):
    __tablename__ = "traders"

    id = Column(Integer, primary_key=True, index=True)
    trader_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    profile_picture = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    social_media_links = Column(Text, nullable=True)
    university = Column(String, index=True)
    department = Column(String, index=True)
    year_of_study = Column(String, index=True)
    business_name = Column(String, index=True)
    business_description = Column(Text, nullable=True)
    category = Column(String, index=True)
    location = Column(String, nullable=True)
    product_listings = Column(Text, nullable=True)  # Could be a JSON string or separate table
    pricing = Column(Text, nullable=True)
    availability = Column(String, nullable=True)
    verification_status = Column(String, default="unverified")
    id_verification = Column(String, default="unverified")
    payment_methods = Column(String, nullable=True)
    response_time = Column(String, nullable=True)
    special_offers = Column(Text, nullable=True)
    portfolio = Column(Text, nullable=True)


