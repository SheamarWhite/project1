"""empty message

Revision ID: db965f1e68cf
Revises: 
Create Date: 2024-03-19 16:05:30.618729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db965f1e68cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('numOfBeds', sa.Integer(), nullable=True),
    sa.Column('numOfBaths', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
