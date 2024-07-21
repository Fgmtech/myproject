
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    APP_NAME: str = "ECOMM"
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_DATABASE: str = os.getenv('POSTGRES_DATABASE')
    SECRET_KEY: str=os.getenv('SECRET_KEY')
    ALGORITHM: str=os.getenv('ALGORITHM')




    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"



settings = Settings()