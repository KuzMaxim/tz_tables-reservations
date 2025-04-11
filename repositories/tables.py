from infrastructure.connect import create_connection, create_tables
from sqlalchemy import select, insert, update, delete
from models.table import Table


class TableRepository:
    def __init__(self):
        self.sessionmaker=create_connection()
        create_tables()
    
    async def create_table(self,id, name, seats, location):
        stmt = insert(Table).values(id=id,
                                    name=name,
                                   seats=seats,
                                   location=location)
        
        async with self.sessionmaker() as session:
            try:
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                raise Exception(f"Can't add user to repository: {e}")

    async def get_tables(self):
        stmt = select(Table)
        
        async with self.sessionmaker() as session:
            try:
                result = await session.execute(stmt)
                row = result.scalars().all()
            except Exception as e:
                raise Exception(f"Couldn't get tables: {e}")
            
        
        if row is None:
            raise Exception(f"No tables found")
        else:
                    return [{
            "id": table.id,
            "name": table.name,
            "seats": table.seats,
            "location": table.location
        } for table in row]

    async def delete_table(self, id):
        stmt=delete().where(Table.id==id)
        
        async with self.sessionmaker() as session:
            try:
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                raise Exception(f"Couldn't delete table: {e}")
            