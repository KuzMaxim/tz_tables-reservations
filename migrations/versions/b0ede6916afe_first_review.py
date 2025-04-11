"""first review

Revision ID: b0ede6916afe
Revises: 
Create Date: 2025-04-10 19:29:16.856171

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision: str = 'b0ede6916afe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    inspector = inspect(op.get_bind())
    
    # Only create tables if they don't exist
    if not inspector.has_table('reservations'):
        op.create_table('reservations',
            sa.Column('id', sa.UUID(), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )
    
    if not inspector.has_table('tables'):
        op.create_table('tables',
            sa.Column('id', sa.UUID(), nullable=False),
            sa.Column('name', sa.String(), nullable=True),
            sa.Column('seats', sa.Integer(), nullable=True),
            sa.Column('location', sa.String(), nullable=True),
            sa.PrimaryKeyConstraint('id')
        )


def downgrade() -> None:
    """Downgrade schema."""
    # Only drop tables if they exist
    op.drop_table('tables', if_exists=True)
    op.drop_table('reservations', if_exists=True)