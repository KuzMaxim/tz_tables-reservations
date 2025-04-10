from repositories.tables import TableRepository
class TableService:
    def __init__(self):
        self.repository = TableRepository()
        
    async def get_tables(self):
        await self.repository.get_tables()
    
    async def create_table(self, name, seats:int, location):
        await self.repository.create_table(name=name, seats=int(seats), location=location)
    
    async def delete_table(self):
        await self.repository.delete_table()