"""remove infection type from report

Revision ID: d562d6bb45a4
Revises: f5f30afe3766
Create Date: 2021-11-27 17:11:37.625304

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd562d6bb45a4'
down_revision = 'f5f30afe3766'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    op.add_column('report', sa.Column('mask_worn', sa.Boolean(), nullable=False))
    op.alter_column('report', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               autoincrement=True)
    op.drop_index('ix_report_infection_type', table_name='report')
    op.create_index(op.f('ix_report_mask_worn'), 'report', ['mask_worn'], unique=False)
    op.drop_column('report', 'infection_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('report', sa.Column('infection_type', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_report_mask_worn'), table_name='report')
    op.create_index('ix_report_infection_type', 'report', ['infection_type'], unique=False)
    op.alter_column('report', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               autoincrement=True)
    op.drop_column('report', 'mask_worn')
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
    # ### end Alembic commands ###
