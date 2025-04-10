from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from services.tables import TableService

router = APIRouter(
    prefix="/tables",
    tags=["Tables"]
)

table_service=TableService()

@router.get("/")
async def get_tables():
    try:
        return await table_service.get_tables()
    except Exception as e:
        return f"Oooops:{e}"
    
@router.post("/")
async def create_table(name, seats, location):
    try:
        await table_service.create_table(name=name, seats=seats, location=location)
    except Exception as e:
        return f"Oooops:{e}"
    
@router.delete("/{table_id}")
async def delete_table():
    try:
        await table_service.delete_table()
    except Exception as e:
        return f"Oooops:{e}"