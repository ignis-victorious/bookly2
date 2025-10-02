#
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#

# In the original text this file is called schemas.py and is inside src/books which also contain a __init__.py


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
