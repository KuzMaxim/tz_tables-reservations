from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, UUID
from uuid import uuid4


class Reservation(Base):
    __tablename__="reservations"
    
    id=Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    table_id=Column(UUID(as_uuid=True), ForeignKey("tables.id"))
    
    table_id=relationship("Table", back_populates="reservations")