"""datetime was added to revision

Revision ID: ecc1c6d89b67
Revises: b0ede6916afe
Create Date: 2025-04-11 00:30:04.553925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecc1c6d89b67'
down_revision: Union[str, None] = 'b0ede6916afe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservations', sa.Column('reservation_time', sa.DateTime(), nullable=True))
    op.add_column('reservations', sa.Column('duration', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservations', 'duration')
    op.drop_column('reservations', 'reservation_time')
    # ### end Alembic commands ###
