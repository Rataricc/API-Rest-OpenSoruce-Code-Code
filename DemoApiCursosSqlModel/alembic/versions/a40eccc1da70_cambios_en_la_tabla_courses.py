"""cambios en la tabla courses

Revision ID: a40eccc1da70
Revises: 6fa5059e20ff
Create Date: 2023-10-09 22:59:54.640793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a40eccc1da70'
down_revision: Union[str, None] = '6fa5059e20ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###