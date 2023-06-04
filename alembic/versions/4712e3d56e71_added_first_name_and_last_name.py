"""added first_name and last_name

Revision ID: 4712e3d56e71
Revises: 3bc988f4d7a2
Create Date: 2023-06-04 14:37:27.489087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4712e3d56e71'
down_revision = '3bc988f4d7a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('authors', sa.Column('first_name', sa.String(length=50), nullable=True))
    op.add_column('authors', sa.Column('last_name', sa.String(length=50), nullable=True))


def downgrade() -> None:
    op.drop_column('authors', 'last_name')
    op.drop_column('authors', 'first_name')
