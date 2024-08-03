
from sqlalchemy import Column, String
from database.db import Base

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    buyer_or_seller = Column(String, nullable=False)  # Add role field to differentiate between buyer and seller