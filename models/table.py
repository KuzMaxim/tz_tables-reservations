from base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, UUID
from uuid import uuid4


class Table(Base):
    __tablename__="tables"
    
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid4)
    
    reservations=relationship("Reservation", back_populates="table")