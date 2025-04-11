from repositories.reservations import ReservationRepository
class ReservationService:
    def __init__(self):
        self.repository = ReservationRepository()
            
    async def get_reservations(self):
        await self.repository.get_reservations()
    
    async def create_reservarion(self,time_reservation, duration, table_id):
        await self.repository.create_reservation(time_reservation=time_reservation, duration=int(duration), table_id=int(table_id))
    
    async def delete_reservation(self, id):
        await self.repository.delete_reservation(id=int(id))