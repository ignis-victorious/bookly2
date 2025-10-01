#
#  Import LIBRARIES
from fastapi import FastAPI, Header

#  Import FILES
from models.bk_models import BookCreate

#


app = FastAPI()


@app.get(path="/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello world!"}


#  Query with Path Parameters
# @app.get(path="/greet/{name}")
# async def greet_name(name: str) -> dict[str, str]:
#     return {"message": f"Hello {name}"}


#  Query with Query Parameters
# @app.get(path="/greet/")
# async def greet_name(name: str) -> dict[str, str]:
#     return {"message": f"Hello {name}"}


#  Mixed query Path + Query Parameters
# @app.get(path="/greet/{name}")
# async def greet_name(name: str, age: int) -> dict[str, str]:
# return {"message": f"Hello {name}, you are {age} years old"}


#  Query default Parameters
@app.get(path="/greet")
async def greet_name(name: str = "User", age: int = 0) -> dict[str, str]:
    return {"message": f"Hello {name}, you are {age} years old"}


#  Request
@app.post(path="/create_book")
async def create_book(book_data: BookCreate) -> dict[str, str]:
    return {"title": book_data.title, "author": book_data.author}


# {
#     "title": "Think Python",
#     "author": "Allen B. Downey",,
# }


#  HEADER
@app.get(path="/get_headers", status_code=500)
# @app.get(path="/get_headers", status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = user_agent
    return request_headers


#  __________________________

#
#  Import LIBRARIES
#  Import FILES
#


# def main():
#     print("Hello from bookly!")


# if __name__ == "__main__":
#     main()
