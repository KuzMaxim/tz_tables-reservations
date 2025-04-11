from repositories.reservations import ReservationRepository
from datetime import datetime

class ReservationService:
    def __init__(self):
        self.repository = ReservationRepository()
            
    async def get_reservations(self):
        return await self.repository.get_reservations()
    
    async def create_reservarion(self,time_reservation, duration, table_id):
        time_reservation=datetime.strptime(time_reservation, "%Y-%m-%d %H:%M:%S")
        print(int(duration))
        print(int(table_id))
        await self.repository.create_reservation(time_reservation=(time_reservation), duration=int(duration), table_id=int(table_id))
    
    async def delete_reservation(self, id):
        await self.repository.delete_reservation(id=int(id))