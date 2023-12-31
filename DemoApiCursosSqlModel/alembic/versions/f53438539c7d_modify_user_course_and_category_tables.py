"""modify user, course and category tables

Revision ID: f53438539c7d
Revises: 39589782b51a
Create Date: 2023-10-09 17:10:36.254221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'f53438539c7d'
down_revision: Union[str, None] = '39589782b51a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('categories_course_id_fkey', 'categories', type_='foreignkey')
    op.drop_column('categories', 'course_id')
    op.add_column('courses', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('courses_categories_id_fkey', 'courses', type_='foreignkey')
    op.create_foreign_key(None, 'courses', 'user', ['user_id'], ['id'])
    op.drop_column('courses', 'categories_id')
    op.drop_constraint('user_course_id_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'course_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_course_id_fkey', 'user', 'courses', ['course_id'], ['id'])
    op.add_column('courses', sa.Column('categories_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.create_foreign_key('courses_categories_id_fkey', 'courses', 'coursescategory', ['categories_id'], ['id'])
    op.drop_column('courses', 'user_id')
    op.add_column('categories', sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('categories_course_id_fkey', 'categories', 'coursescategory', ['course_id'], ['id'])
    # ### end Alembic commands ###
