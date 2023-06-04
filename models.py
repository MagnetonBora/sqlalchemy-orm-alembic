import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from session import engine

Base = declarative_base(bind=engine)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    login = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.datetime.now)

    articles = relationship(
        "Article",
        back_populates="author",
        cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return f"Author({self.login})"


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    publication_date = Column(DateTime, default=datetime.datetime.now)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship("Author", back_populates="articles")
    hashtags = relationship(
        "Hashtag",
        back_populates="articles",
        secondary="articles_hashtags"
    )

    def __repr__(self):
        return f"Article({self.title})"


class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    creation_date = Column(DateTime, default=datetime.datetime.now)

    articles = relationship(
        "Article",
        back_populates="hashtags",
        secondary="articles_hashtags"
    )

    def __repr__(self):
        return f"Hashtag({self.name})"


article_hashtag = Table(
    "articles_hashtags",
    Base.metadata,
    Column(
        "article_id",
        Integer,
        ForeignKey("articles.id"),
        primary_key=True
    ),
    Column(
        "hashtag_id",
        Integer,
        ForeignKey("hashtags.id"),
        primary_key=True
    )
)
