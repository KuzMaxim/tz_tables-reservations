from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Table(Base):
    __tablename__ = "tables"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    seats = Column(Integer)
    location = Column(String)
    
    reservations = relationship("Reservation", back_populates="table")