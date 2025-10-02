#
#  Import LIBRARIES
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException

#  Import FILES
# from models.bk_models import BookCreate
from db.book_db import books
from models.bk_models import Book, BookUpdate

#


app: FastAPI = FastAPI()


@app.get(path="/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello world!"}


# Return all books - without Pydantic model
# @app.get(path="/books")
# async def get_all_books() -> list[dict[str, int | str]]:
#     return books
# Return all book but with Pydantic model
@app.get(path="/books", response_model=list[Book])
async def get_all_books() -> list[Book]:
    return books


@app.post(path="/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> Book:
    new_book: Book = book_data
    # new_book: Book = book_data.model_dump # Use if books os still a list of Dict model_dump transform into a dict
    books.append(new_book)
    return new_book


@app.get(path="/book/{book_id}")
async def get_book(book_id: int) -> Book | None:
    for book in books:
        if book_id == book.id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.patch(path="/book/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdate):
    for book in books:
        if book.id == book_id:
            book.title = book_update_data.title
            book.publisher = book_update_data.publisher
            book.page_count = book_update_data.page_count
            book.language = book_update_data.language
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete(path="/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


#  __________________________

#
#  Import LIBRARIES
#  Import FILES
#


# def main():
#     print("Hello from bookly!")


# if __name__ == "__main__":
#     main()
