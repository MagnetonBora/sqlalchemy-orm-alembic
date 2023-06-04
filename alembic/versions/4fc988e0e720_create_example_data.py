"""create example data

Revision ID: 4fc988e0e720
Revises: 576d72a624eb
Create Date: 2023-06-04 15:25:00.344966

"""
from random import choice

from faker import Faker
from sqlalchemy.exc import IntegrityError

from models import Author, Article, Hashtag, Base
from session import session

# revision identifiers, used by Alembic.
revision = '4fc988e0e720'
down_revision = '576d72a624eb'
branch_labels = None
depends_on = None


def create_authors(count=50):
    fake = Faker()
    return [
        Author(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            login=fake.user_name(),
            email=fake.email(),
        )
        for _ in range(count)
    ]


def create_article(author_id):
    fake = Faker()
    return Article(
        title=fake.sentence(),
        content=fake.text(),
        author_id=author_id,
    )


def create_articles(author_id, count=10):
    return [
        create_article(author_id)
        for _ in range(count)
    ]


def create_hashtags(count=10):
    fake = Faker()

    hashtags = set()
    while len(hashtags) < count:
        hashtags.add(fake.word())

    return [
        Hashtag(name=hashtag)
        for hashtag in hashtags
    ]


def assign_hashtags_to_articles(hashtags, articles):
    for article in articles:
        hashtag = choice(hashtags)
        article.hashtags.append(hashtag)


def upgrade() -> None:
    # Create authors
    authors = create_authors(count=1000)
    for author in authors:
        print(f"Adding author {author.login}")
        try:
            session.add(author)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"Author {author.login} already exists")

    # Create articles
    author = choice(authors)
    articles = create_articles(author_id=author.id)
    session.add_all(articles)
    session.commit()

    # Create hashtags
    hashtags = create_hashtags(count=100)
    try:
        session.add_all(hashtags)
        session.commit()
    except IntegrityError:
        session.rollback()

    # Assign hashtags to articles
    try:
        assign_hashtags_to_articles(hashtags, articles)
        session.commit()
    except IntegrityError:
        session.rollback()


def downgrade() -> None:
    metadata = Base.metadata
    for table in reversed(metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()
