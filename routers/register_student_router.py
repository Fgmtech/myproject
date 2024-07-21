
from fastapi import FastAPI, HTTPException, Form, UploadFile, File, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Optional
import os
import bcrypt
from models.register_student import Student


router = APIRouter()

# Example in-memory database
students_db: Dict[str, Student] = {}

@router.post("/register-student/")
async def register_student(
    student_id: str = Form(...),
    name: str = Form(...),
    password: str = Form(...),
    id_image: UploadFile = File(...)
):
    if student_id in students_db:
        raise HTTPException(status_code=400, detail="Student already registered")
    
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Ensure the images directory exists
    os.makedirs("images", exist_ok=True)
    
    # Save the uploaded image
    image_path = f"images/{student_id}_{id_image.filename}"
    try:
        with open(image_path, "wb") as image_file:
            content = await id_image.read()
            image_file.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save image: {str(e)}")
    
    # Add student to the database
    student = Student(student_id=student_id, name=name, id_image_path=image_path, hashed_password=hashed_password)
    students_db[student_id] = student

    return JSONResponse(content={"message": "Student registered successfully", "student": student.dict()})


@router.post("/login/")
async def login_student(
    student_id: str = Form(...),
    password: str = Form(...)
):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=401, detail="Invalid student ID or password")
    
    if not bcrypt.checkpw(password.encode('utf-8'), student.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid student ID or password")
    
    return JSONResponse(content={"message": "Login successful", "student": student.dict()})


