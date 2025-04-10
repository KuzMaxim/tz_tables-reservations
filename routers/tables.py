from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from services.tables import TableService
router = APIRouter(
    prefix="/tables",
    tags=["Tables"]
)

@router.get("/")
async def get_tables():
    ...
    
@router.post("/")
async def create_table():
    ...
    
@router.delete("/{table_id}")
async def delete_table():
    ...