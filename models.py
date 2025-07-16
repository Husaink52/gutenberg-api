from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Association tables
book_authors = Table(
    "books_book_authors", Base.metadata,
    Column("book_id", Integer, ForeignKey("books_book.id")),
    Column("author_id", Integer, ForeignKey("books_author.id"))
)

book_bookshelves = Table(
    "books_book_bookshelves", Base.metadata,
    Column("book_id", Integer, ForeignKey("books_book.id")),
    Column("bookshelf_id", Integer, ForeignKey("books_bookshelf.id"))
)

book_subjects = Table(
    "books_book_subjects", Base.metadata,
    Column("book_id", Integer, ForeignKey("books_book.id")),
    Column("subject_id", Integer, ForeignKey("books_subject.id"))
)

book_languages = Table(
    "books_book_languages", Base.metadata,
    Column("book_id", Integer, ForeignKey("books_book.id")),
    Column("language_id", Integer, ForeignKey("books_language.id"))
)

# Core models
class Author(Base):
    __tablename__ = "books_author"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Bookshelf(Base):
    __tablename__ = "books_bookshelf"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Subject(Base):
    __tablename__ = "books_subject"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Language(Base):
    __tablename__ = "books_language"
    id = Column(Integer, primary_key=True)
    code = Column(String)

class Format(Base):
    __tablename__ = "books_format"
    id = Column(Integer, primary_key=True)
    mime_type = Column(String)
    url = Column(String)
    book_id = Column(Integer, ForeignKey("books_book.id"))

class Book(Base):
    __tablename__ = "books_book"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    download_count = Column(Integer)

    authors = relationship("Author", secondary=book_authors, backref="books")
    bookshelves = relationship("Bookshelf", secondary=book_bookshelves, backref="books")
    subjects = relationship("Subject", secondary=book_subjects, backref="books")
    languages = relationship("Language", secondary=book_languages, backref="books")
    formats = relationship("Format", backref="book")
