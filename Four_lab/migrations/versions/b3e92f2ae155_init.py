"""Init

Revision ID: b3e92f2ae155
Revises: bank
Create Date: 2023-05-11 11:26:09.652735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3e92f2ae155'
down_revision = 'bank'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('acounts', 'date_open')
    op.drop_column('acounts', 'date_close')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('acounts', sa.Column('date_close', sa.DATE(), nullable=True))
    op.add_column('acounts', sa.Column('date_open', sa.DATE(), nullable=True))
    # ### end Alembic commands ###
