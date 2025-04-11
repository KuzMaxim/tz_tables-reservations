"""reservations id from uuid to integer

Revision ID: b16703e1895e
Revises: 4f27372dc894
Create Date: 2025-04-11 12:59:03.623692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b16703e1895e'
down_revision: Union[str, None] = '4f27372dc894'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Create a sequence for the new integer IDs
    op.execute(sa.schema.CreateSequence(sa.Sequence('reservations_id_seq')))
    
    # 2. Add a new temporary integer column
    op.add_column('reservations', sa.Column('new_id', sa.Integer(), 
                  server_default=sa.text("nextval('reservations_id_seq')"),
                  nullable=False))
    
    # 3. Drop primary key constraint
    op.drop_constraint('reservations_pkey', 'reservations', type_='primary')
    
    # 4. Drop the old UUID column
    op.drop_column('reservations', 'id')
    
    # 5. Rename new column to id
    op.alter_column('reservations', 'new_id', new_column_name='id')
    
    # 6. Recreate primary key
    op.create_primary_key('reservations_pkey', 'reservations', ['id'])
    
    # 7. Set sequence ownership
    op.execute('ALTER SEQUENCE reservations_id_seq OWNED BY reservations.id')


def downgrade() -> None:
    # 1. Add a temporary UUID column
    op.add_column('reservations', sa.Column('old_id', postgresql.UUID(), 
                  server_default=sa.text('gen_random_uuid()'),
                  nullable=False))
    
    # 2. Drop primary key constraint
    op.drop_constraint('reservations_pkey', 'reservations', type_='primary')
    
    # 3. Drop the integer column
    op.drop_column('reservations', 'id')
    
    # 4. Rename old column to id
    op.alter_column('reservations', 'old_id', new_column_name='id')
    
    # 5. Recreate primary key
    op.create_primary_key('reservations_pkey', 'reservations', ['id'])
    
    # 6. Drop the sequence
    op.execute(sa.schema.DropSequence(sa.Sequence('reservations_id_seq')))