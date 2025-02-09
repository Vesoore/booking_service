from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.booking import BookingCreate
from app.models import Booking

router = APIRouter()

@router.post("/book/")
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):

    if booking.start_time >= booking.end_time:
        raise HTTPException(status_code=400, detail="Invalid time range")

    # Check for overlapping bookings
    overlapping_booking = db.query(Booking).filter(
        and_(
            Booking.start_time < booking.end_time,
            Booking.end_time > booking.start_time
        )
    ).first()

    if overlapping_booking:
        raise HTTPException(status_code=400, detail="Time slot is already booked")

    new_booking = Booking(start_time=booking.start_time, end_time=booking.end_time)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@router.get("/")
def get_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()

@router.get("/{booking_id}")
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(booking)
    db.commit()
    return {"message": "Booking deleted successfully"}