"""Added required tables

Revision ID: 26fcfdfca49b
Revises: 
Create Date: 2022-05-30 12:46:03.064447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26fcfdfca49b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emai', sa.String(length=40), nullable=True),
    sa.Column('user_name', sa.String(length=100), nullable=True),
    sa.Column('user_data', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_emai'), 'users', ['emai'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_emai'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###