from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from services.tables import TableService
router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)

@router.get("/")
async def get_reservations():
    ...
    
@router.post("/")
async def create_reservation():
    ...
    
@router.delete("/{table_id}")
async def delete_reservation():
    ...