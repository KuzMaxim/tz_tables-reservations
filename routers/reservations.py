from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from services.reservations import ReservationService

reservation_service=ReservationService()

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)

@router.get("/")
async def get_reservations():
    try:
        await reservation_service.get_reservations()
    except Exception as e:
        return f"Ooops: {e}"
@router.post("/")
async def create_reservation(time_reservation, duration, table_id):
    try:
        await reservation_service.create_reservarion(time_reservation=time_reservation, duration=duration, table_id=table_id)
    except Exception as e:
        return f"Ooops: {e}"

@router.delete("/{table_id}")
async def delete_reservation(id):
    try:
        await reservation_service.delete_reservation(id=id)
    except Exception as e:
        return f"Ooops: {e}"