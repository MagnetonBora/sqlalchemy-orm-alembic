"""add all tables

Revision ID: 6c731184ea28
Revises: 696f1181c90f
Create Date: 2023-06-04 15:11:28.470734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c731184ea28'
down_revision = '696f1181c90f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'hashtags',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('creation_date', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('publication_date', sa.DateTime(), nullable=True),
        sa.Column('author_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('title')
    )
    op.create_table(
        'articles_hashtags',
        sa.Column('article_id', sa.Integer(), nullable=False),
        sa.Column('hashtag_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
        sa.ForeignKeyConstraint(['hashtag_id'], ['hashtags.id'], ),
        sa.PrimaryKeyConstraint('article_id', 'hashtag_id')
    )
    op.add_column('authors', sa.Column('registration_date', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('authors', 'registration_date')
    op.drop_table('articles_hashtags')
    op.drop_table('articles')
    op.drop_table('hashtags')
