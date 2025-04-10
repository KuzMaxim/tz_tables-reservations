from repositories.reservations import ReservationRepository
class ReservationService:
    def __init__(self):
        self.repository = ReservationRepository()
            
    async def get_reservations(self):
        await self.repository.get_reservations()
    
    async def create_reservarion(self):
        await self.repository.create_reservation()
    
    async def delete_reservation(self, id):
        await self.repository.delete_reservation(id=id)