"""Renaming name column to full_name

Revision ID: 2875c22ea5cf
Revises: efb6d425bfa9
Create Date: 2024-01-21 19:58:30.876692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2875c22ea5cf'
down_revision = 'efb6d425bfa9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='full_name')


def downgrade() -> None:
    op.alter_column('scholars', 'full_name', new_column_name='name')
