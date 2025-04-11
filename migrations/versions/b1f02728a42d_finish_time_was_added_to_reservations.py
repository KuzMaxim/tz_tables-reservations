"""finish_time was added to reservations

Revision ID: b1f02728a42d
Revises: b16703e1895e
Create Date: 2025-04-11 15:00:48.805288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1f02728a42d'
down_revision: Union[str, None] = 'b16703e1895e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservations', sa.Column('finish_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservations', 'finish_time')
    # ### end Alembic commands ###
