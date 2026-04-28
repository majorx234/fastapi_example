from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 8000
    allowed_origins: List[str] = ["http://0.0.0.0:8000"]

    db_name: str = Field(default="testdb")
    db_user: str = Field(default="dbuser")
    db_password: str = Field(min_length=5, max_length=30)
