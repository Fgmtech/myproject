

from fastapi import FastAPI, HTTPException, Form, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Optional
import os
import bcrypt


class Student(BaseModel):
    student_id: str
    name: str
    id_image_path: Optional[str] = None
    hashed_password: str