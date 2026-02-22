"""empty message

Revision ID: ebb8ccafd11c
Revises: ad5fd8e18f68
Create Date: 2026-02-22 18:48:27.551942

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ebb8ccafd11c'
down_revision = 'ad5fd8e18f68'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('order_item', 'price_at_purchase')
    op.add_column('order_item', sa.Column('price_at_purchase', sa.Float(), nullable=False))

def downgrade():
    op.drop_column('order_item', 'price_at_purchase')
    op.add_column('order_item', sa.Column('price_at_purchase', sa.TIMESTAMP(), nullable=False))
