from fastapi import APIRouter
from app.api.endpoints import booking
from app.api.endpoints import users
api_router = APIRouter(prefix="/api")

api_router.include_router(booking.router,prefix="/bookings", tags=["bookings"])
api_router.include_router(users.router,prefix="/users", tags=["users"])
