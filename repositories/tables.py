from infrastructure.connect import create_connection, create_tables
from sqlalchemy import select, insert, update
from models.table import Table


class TableRepository:
    def __init__(self):
        self.sessionmaker=create_connection()
        create_tables()
    
    async def create_table(self, name, seats, location):
        stmt = insert(Table).values(name=name,
                                   seats=seats,
                                   location=location)
        
        async with self.sessionmaker() as session:
            try:
                await session.execute(stmt)
                await session.commit()
            except Exception as ex:
                raise Exception(f"Can't add user to repository: {ex}")

    async def get_tables(self, email: str) -> str:
        stmt = select(Table.id).where(Table.email == email)
        
        async with self.sessionmaker() as session:
            try:
                result = await session.execute(stmt)
                row = result.fetchone()
            except Exception as e:
                raise Exception(f"Не удалось получить пользователя: {str(e)}")
            
        
        if row is None:
            raise Exception(f"No user with email: {email}")
        else:
            return str(row[0])

    async def delete_table():
        ...