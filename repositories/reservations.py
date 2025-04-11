from infrastructure.connect import create_connection, create_tables
from sqlalchemy import select, insert, update, delete, and_
from models.reservation import Reservation
from datetime import datetime, timedelta
from sqlalchemy.sql.expression import func  # Add this import


class ReservationRepository:
    def __init__(self):
        self.sessionmaker = create_connection()
        create_tables()

    async def is_table_available(self, table_id: int, reservation_time: datetime, duration: int) -> bool:
        end_time = datetime(reservation_time) + timedelta(minutes=duration)
        
        stmt = select(Reservation).where(
            and_(
                Reservation.table_id == table_id,
                Reservation.reservation_time < end_time,
                func.make_interval(mins=Reservation.duration) + Reservation.reservation_time > reservation_time
            )
        )
        
        async with self.sessionmaker() as session:
            try:
                result = await session.execute(stmt)
                existing_reservations = result.scalars().all()
            except Exception as e:
                raise Exception(f"Error while trying to check available time: {e}")

        return len(existing_reservations) == 0
    
    async def create_reservation(self, time_reservation: datetime, duration: int, table_id: int):
        if not await self.is_table_available(table_id=table_id, reservation_time=time_reservation, duration=duration):
            raise Exception("Time is not available")
            
        stmt = insert(Reservation).values(
            table_id=table_id,
            reservation_time=time_reservation,
            duration=duration
        )
        
        async with self.sessionmaker() as session:
            try:
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise Exception(f"Couldn't create reservation: {e}")
            
    async def get_reservations(self):
        stmt = select(Reservation)
        
        async with self.sessionmaker() as session:
            try:
                result = await session.execute(stmt)
                reservations = result.scalars().all()
            except Exception as e:
                raise Exception(f"Couldn't get reservations: {e}")
        
        if not reservations:
            return []
            
        return [{
            "id": reservation.id,
            "table_id": reservation.table_id,
            "reservation_time": reservation.reservation_time,
            "duration": reservation.duration
        } for reservation in reservations]

    async def delete_reservation(self, id: int):
        stmt = delete(Reservation).where(Reservation.id == id)
        
        async with self.sessionmaker() as session:
            try:
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise Exception(f"Couldn't delete reservation: {e}")