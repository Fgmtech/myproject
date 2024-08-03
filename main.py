
#from fastapi import FastAPI, File, UploadFile, Form, HTTPException
#from fastapi.responses import JSONResponse
#from pydantic import BaseModel
#from typing import Optional

#app = FastAPI()

#class Student(BaseModel):
    #student_id: str
    #name: Optional[str] = None

# Example in-memory database
#students_db = {
    #"12345": {"name": "Alice"},
    #"67890": {"name": "Bob"},
#}

#@app.post("/verify-student/")
#async def verify_student(student_id: str = Form(...), id_image: UploadFile = File(...)):
    #if student_id not in students_db:
        #raise HTTPException(status_code=404, detail="Student not found")
    
    #student = students_db[student_id]

    # For demonstration, we'll assume the verification is always successful
    # Here, you would add the actual image verification logic
    # E.g., using an image recognition API or library

    #return JSONResponse(content={"message": "Student verified", "student": student})

#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="127.0.0.1", port=8000)




#from fastapi import FastAPI, File, UploadFile, Form, HTTPException
#from fastapi.responses import JSONResponse
#from pydantic import BaseModel
#from typing import Optional, Dict
#from routers import user

#app = FastAPI()

#class Student(BaseModel):
    #student_id: str
    #name: str
    #id_image_path: Optional[str] = None

# Example in-memory database
#students_db: Dict[str, Student] = {}

#@app.post("/register-student/")
#async def register_student(
    #student_id: str = Form(...),
    #name: str = Form(...),
    #id_image: UploadFile = File(...)
#):
    #if student_id in students_db:
        #raise HTTPException(status_code=400, detail="Student already registered")
    
    # Save the uploaded image
    #image_path = f"images/{student_id}_{id_image.filename}"
    #with open(image_path, "wb") as image_file:
        #content = await id_image.read()
        #image_file.write(content)
    
    # Add student to the database
    #student = Student(student_id=student_id, name=name, id_image_path=image_path)
    #students_db[student_id] = student

    #return JSONResponse(content={"message": "Student registered successfully", "student": student.dict()})

#@app.post("/verify-student/")
#async def verify_student(
    #student_id: str = Form(...),
    #id_image: Optional[UploadFile] = File(None)
#):
    #if student_id not in students_db:
        #raise HTTPException(status_code=404, detail="Student not found")
    
    #student = students_db[student_id]

    #if id_image:
        # Perform image verification logic
        # For demonstration, we'll assume the verification is always successful
        #pass

    #return JSONResponse(content={"message": "Student verified", "student": student.dict()})

#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="127.0.0.1", port=8000)


from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict
from database.db import engine, Base
from routers import register_student_router, trader_profile_router, register_buyer_seller_router, product_router
from database.db import Base, get_db
from sqlalchemy.orm import sessionmaker, Session




app = FastAPI()


Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(register_student_router.router)
app.include_router(trader_profile_router.router)
app.include_router(register_buyer_seller_router.router, prefix="/user", tags=["user"])
app.include_router(product_router.router)







if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
