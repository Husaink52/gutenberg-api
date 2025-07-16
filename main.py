from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import SessionLocal
import crud

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books")
def get_books(
    db: Session = Depends(get_db),
    book_id: Optional[List[int]] = Query(None),
    language: Optional[List[str]] = Query(None),
    mime_type: Optional[List[str]] = Query(None),
    topic: Optional[List[str]] = Query(None),
    author: Optional[str] = None,
    title: Optional[str] = None,
    page: int = 1
):
    return crud.get_filtered_books(
        db=db,
        book_ids=book_id,
        languages=language,
        mime_types=mime_type,
        topics=topic,
        author=author,
        title=title,
        page=page
    )
