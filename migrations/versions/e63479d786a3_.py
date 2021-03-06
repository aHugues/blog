"""empty message

Revision ID: e63479d786a3
Revises: 81281bca10b9
Create Date: 2018-09-01 18:24:00.610022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e63479d786a3'
down_revision = '81281bca10b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Articles', sa.Column('content', sa.Text(), nullable=True))
    op.add_column('Articles', sa.Column('date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Articles', 'date')
    op.drop_column('Articles', 'content')
    # ### end Alembic commands ###
