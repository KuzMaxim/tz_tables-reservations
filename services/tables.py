from repositories.tables import TableRepository
class TableService:
    def __init__(self):
        self.repository = TableRepository()
        
    async def get_tables(self):
        return await self.repository.get_tables()
    
    async def create_table(self,id:int, name, seats:int, location):
        await self.repository.create_table(id=int(id),name=name, seats=int(seats), location=location)
    
    async def delete_table(self, id:int):
        await self.repository.delete_table(id=int(id))