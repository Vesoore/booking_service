from typing import List
from pydantic import BaseModel, EmailStr, Field
from app.schemas.booking import BookingCreate

class UserCreate(BaseModel):
    name: str = Field(..., description="User's name")
    email: EmailStr = Field(..., description="User's email")

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    bookings: List[BookingCreate] = []

    class Config:
        from_attributes = True