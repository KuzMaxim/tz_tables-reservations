from fastapi import FastAPI
from routers import tables, reservations

app=FastAPI(
    title="TestWeb"
)

app.include_router(tables.router)
app.include_router(reservations.router)