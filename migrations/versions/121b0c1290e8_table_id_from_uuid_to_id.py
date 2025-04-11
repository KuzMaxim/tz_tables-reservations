"""table_id from uuid to id

Revision ID: 121b0c1290e8
Revises: ecc1c6d89b67
Create Date: 2025-04-11 11:41:14.070186

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '121b0c1290e8'
down_revision = 'ecc1c6d89b67'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. Добавляем новый временный столбец integer
    op.add_column('tables', sa.Column('new_id', sa.Integer(), nullable=True))
    
    # 2. Заполняем новый столбец значениями (например, последовательными числами)
    op.execute('UPDATE tables SET new_id = nextval(pg_get_serial_sequence(\'tables\', \'new_id\'))')
    
    # 3. Удаляем первичный ключ
    op.drop_constraint('tables_pkey', 'tables', type_='primary')
    
    # 4. Удаляем старый столбец UUID
    op.drop_column('tables', 'id')
    
    # 5. Переименовываем new_id в id
    op.alter_column('tables', 'new_id', new_column_name='id')
    
    # 6. Устанавливаем новый первичный ключ
    op.create_primary_key('tables_pkey', 'tables', ['id'])


def downgrade() -> None:
    # 1. Добавляем временный столбец UUID
    op.add_column('tables', sa.Column('old_id', postgresql.UUID(), nullable=True))
    
    # 2. Заполняем его какими-то UUID значениями (здесь нужно ваше решение)
    # Например, можно генерировать новые UUID:
    op.execute('UPDATE tables SET old_id = gen_random_uuid()')
    
    # 3. Удаляем первичный ключ
    op.drop_constraint('tables_pkey', 'tables', type_='primary')
    
    # 4. Удаляем столбец integer
    op.drop_column('tables', 'id')
    
    # 5. Переименовываем old_id в id
    op.alter_column('tables', 'old_id', new_column_name='id')
    
    # 6. Устанавливаем старый первичный ключ
    op.create_primary_key('tables_pkey', 'tables', ['id'])