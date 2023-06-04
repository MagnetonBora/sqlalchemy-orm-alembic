"""added salary and email

Revision ID: 696f1181c90f
Revises: 4712e3d56e71
Create Date: 2023-06-04 14:41:49.836826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '696f1181c90f'
down_revision = '4712e3d56e71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('authors', sa.Column('salary', sa.Float(), nullable=True))
    op.add_column('authors', sa.Column('email', sa.String(length=50), nullable=False))
    op.create_unique_constraint("uniq_email", 'authors', ['email'])


def downgrade() -> None:
    op.drop_constraint("uniq_email", 'authors', type_='unique')
    op.drop_column('authors', 'email')
    op.drop_column('authors', 'salary')
