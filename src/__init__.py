# #
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from src.books.routes import bk_router

#


version: str = "v1"
app: FastAPI = FastAPI(
    title="Bookly",
    description="A RESTful API for a book review web service",
    version=version,
    # lifespan=life_span
)

app.include_router(router=bk_router, prefix=f"/api/{version}/books", tags=["books"])
# app.include_router(router=bk_router, prefix="/books")
