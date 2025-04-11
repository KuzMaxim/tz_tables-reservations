from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, UUID, DateTime, Integer
from uuid import uuid4


class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    reservation_time = Column(DateTime)
    finish_time=Column(DateTime)
    duration = Column(Integer)
    
    table = relationship("Table", back_populates="reservations")