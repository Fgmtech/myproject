


from datetime import datetime 
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Form, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from typing import List, Optional, Any
from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from config.config import settings
from database.db import Base, get_db



class Product(Base):
    __tablename__ = "products"

    trader_id = Column(String, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    product_name = Column(String, index=True)
    description = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    

