"""prevent null on access_code

Revision ID: 8d328b345bfd
Revises: dbd83c3d328c
Create Date: 2021-11-10 11:10:23.933821

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8d328b345bfd'
down_revision = 'dbd83c3d328c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('organization', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               autoincrement=True)
    op.alter_column('path', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               autoincrement=True)
    op.alter_column('point', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               autoincrement=True)
    op.alter_column('report', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('report', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               autoincrement=True)
    op.alter_column('point', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               autoincrement=True)
    op.alter_column('path', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               autoincrement=True)
    op.alter_column('organization', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
