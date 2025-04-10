from infrastructure.connect import create_connection, create_tables
from sqlalchemy import select, insert, update, delete
from models.reservation import Reservation


class ReservationRepository:
    def __init__(self):
        self.sessionmaker=create_connection()
        create_tables()

    async def create_reservation(self, email:str, name:str, yandex_id:int, is_superuser:bool, id):
        stmt = insert(Reservation).values(id=id,
                                   email=email,
                                   name=name,
                                   yandex_id=yandex_id,
                                   is_superuser=is_superuser)
        
        async with self.sessionmaker() as session:
            try:
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                raise Exception(f"Can't add user to repository: {e}")

    async def get_reservations(self, id):
        stmt = select(Reservation.table_id).where(Reservation.id == id)
        
        async with self.sessionmaker() as session:
            try:
                result = await session.execute(stmt)
                row = result.fetchall()
            except Exception as e:
                raise Exception(f"Couldn't get reservation because of {e}")
            
        
        if row is None:
            raise Exception(f"There is no such reservation")
        else:
            return row

    async def delete_reservation(self, id):
        stmt=delete().where(Reservation.id==id)
        
        async with self.sessionmaker() as session:
            try:
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                raise Exception(f"Couldn't delete reservation because of {e}")