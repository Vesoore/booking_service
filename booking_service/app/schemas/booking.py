from pydantic import BaseModel, Field
from datetime import datetime

# Define Pydantic model for request validation
class BookingCreate(BaseModel):
    start_time: datetime = Field(..., description="Start time of the booking")
    end_time: datetime = Field(..., description="End time of the booking")
    user_id: int = Field(..., description="ID of the user making the booking")
