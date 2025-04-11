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
         result=await table_service.get_tables()
    except Exception as e:
        return f"Oooops:{e}"
    return result
    
@router.post("/")
async def create_table(id, name, seats, location):
    try:
        await table_service.create_table(id=id,name=name, seats=seats, location=location)
    except Exception as e:
        return f"Oooops:{e}"
    return "success"

@router.delete("/{table_id}")
async def delete_table(table_id:int):
    try:
        await table_service.delete_table(id=table_id)
    except Exception as e:
        return f"Oooops:{e}"
    return "success"