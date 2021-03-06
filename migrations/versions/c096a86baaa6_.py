"""empty message

Revision ID: c096a86baaa6
Revises: 
Create Date: 2018-01-29 08:00:34.163205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c096a86baaa6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
