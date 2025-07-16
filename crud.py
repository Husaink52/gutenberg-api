from sqlalchemy.orm import Session
from sqlalchemy import or_
from models import Book, Author, Format, Subject, Bookshelf, Language

def get_filtered_books(
    db: Session,
    book_ids=None,
    languages=None,
    mime_types=None,
    topics=None,
    author=None,
    title=None,
    page=1
):
    query = db.query(Book).distinct()

    if mime_types:
        query = query.join(Book.formats)
    if topics:
        query = query.outerjoin(Book.subjects).outerjoin(Book.bookshelves)
    if author:
        query = query.join(Book.authors)
    if languages:
        query = query.join(Book.languages)

    # Filters
    if book_ids:
        query = query.filter(Book.id.in_(book_ids))

    if languages:
        query = query.filter(Language.code.in_(languages))

    if mime_types:
        mt_filters = [Format.mime_type.ilike(f"%{mt}%") for mt in mime_types]
        query = query.filter(or_(*mt_filters))

    if topics:
        topic_filters = []
        for t in topics:
            topic_filters.extend([
                Subject.name.ilike(f"%{t}%"),
                Bookshelf.name.ilike(f"%{t}%")
            ])
        query = query.filter(or_(*topic_filters))

    if author:
        query = query.filter(Author.name.ilike(f"%{author}%"))

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))

    query = query.order_by(Book.download_count.desc())
    total = query.count()
    books = query.offset((page - 1) * 25).limit(25).all()

    return {
        "total": total,
        "books": [format_book(book) for book in books]
    }

def format_book(book):
    return {
        "id": book.id,
        "title": book.title,
        "authors": [a.name for a in book.authors],
        "languages": [l.code for l in book.languages],
        "subjects": [s.name for s in book.subjects],
        "bookshelves": [b.name for b in book.bookshelves],
        "download_links": [
            {"mime_type": f.mime_type, "url": f.url}
            for f in book.formats
        ]
    }
