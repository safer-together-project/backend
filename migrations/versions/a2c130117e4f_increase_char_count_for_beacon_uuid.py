"""increase char count for beacon uuid

Revision ID: a2c130117e4f
Revises: 06bae504ea49
Create Date: 2021-11-27 14:11:42.408911

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a2c130117e4f'
down_revision = '06bae504ea49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('beacon', 'id',
               existing_type=mysql.VARCHAR(length=35),
               type_=sqlmodel.sql.sqltypes.AutoString(length=36),
               existing_nullable=False)
    op.alter_column('employee', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               autoincrement=True)
    op.alter_column('infection', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               autoincrement=True)
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
    op.alter_column('infection', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               autoincrement=True)
    op.alter_column('employee', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               autoincrement=True)
    op.alter_column('beacon', 'id',
               existing_type=sqlmodel.sql.sqltypes.AutoString(length=36),
               type_=mysql.VARCHAR(length=35),
               existing_nullable=False)
    # ### end Alembic commands ###
