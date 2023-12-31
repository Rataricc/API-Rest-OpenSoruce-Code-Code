"""add relationships from models - add union table courses_category

Revision ID: 39589782b51a
Revises: 78510060c709
Create Date: 2023-10-07 17:56:47.479352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '39589782b51a'
down_revision: Union[str, None] = '78510060c709'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coursescategory',
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('categories', sa.Column('course_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'categories', 'coursescategory', ['course_id'], ['id'])
    op.add_column('courses', sa.Column('categories_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'courses', 'coursescategory', ['categories_id'], ['id'])
    op.add_column('user', sa.Column('course_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'courses', ['course_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'course_id')
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.drop_column('courses', 'categories_id')
    op.drop_constraint(None, 'categories', type_='foreignkey')
    op.drop_column('categories', 'course_id')
    op.drop_table('coursescategory')
    # ### end Alembic commands ###
