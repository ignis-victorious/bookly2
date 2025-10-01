#
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#


class BookCreate(BaseModel):
    title: str
    author: str
