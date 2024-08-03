
from fastapi import HTTPException, Depends
from database.db import Base, get_db
from fastapi import FastAPI, HTTPException, Form, UploadFile, File, Depends, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, String, Integer, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config.config import settings
from models.product import Product
from datetime import datetime


router = APIRouter()


class ProductCreate(BaseModel):
    trader_id : str
    product_id : int
    product_name : str
    description : str
    category : str
    price : float
    quantity : int
    created_at : datetime
    updated_at : datetime
    
    
    
    
    
    
    
    


@router.post("/products/", response_model=ProductCreate)
async def create_product(
    trader_id: str = Form(...),
    product_id: int = Form(...),
    product_name: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    price: float = Form(...),
    quantity: int = Form(...),
    db: Session = Depends(get_db)
 
):
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    
    product = Product(
        
        trader_id = trader_id,
        product_id = product_id,
        product_name = product_name,
        description = description,
        category = category,
        price = price,
        quantity = quantity,
        created_at = created_at,
        updated_at = updated_at
        
    )
    
    db.add(product)
    db.commit()
    db.refresh(product)

    return product



@router.get("/products/{product_id}", response_model=ProductCreate)
async def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
