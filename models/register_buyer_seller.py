
from sqlalchemy import Column, String
from database.db import Base

class User(Base):
    __tablename__ = "users"
    
    ID_number = Column(String, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # Add role field to differentiate between buyer and seller
