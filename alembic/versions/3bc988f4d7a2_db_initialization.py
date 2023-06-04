"""db initialization

Revision ID: 3bc988f4d7a2
Revises: 
Create Date: 2023-06-04 14:24:26.834384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bc988f4d7a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('login', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('login')
    )


def downgrade() -> None:
    op.drop_table('authors')
