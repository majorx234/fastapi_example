from pydantic import BaseModel, Field
from datetime import date


class User(BaseModel):
    name: str
    email: str
    birth_date: date = Field(..., title='Date Of Birth')
