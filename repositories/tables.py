from infrastructure.connect import create_connection, create_tables
from sqlalchemy import select, insert, update
from models.table import Table


class TableRepository:
    def __init__(self):
        self.sessionmaker=create_connection()
        create_tables()
