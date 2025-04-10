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
    await reservation_service.get_reservations()
    
@router.post("/")
async def create_reservation():
    await reservation_service.create_table()
    
@router.delete("/{table_id}")
async def delete_reservation():
    ...