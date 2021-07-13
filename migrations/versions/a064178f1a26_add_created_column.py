"""add created column

Revision ID: a064178f1a26
Revises: c91e607c8ff0
Create Date: 2021-07-13 14:40:27.593299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a064178f1a26'
down_revision = 'c91e607c8ff0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('measurements', sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('measurements', 'created')
    # ### end Alembic commands ###