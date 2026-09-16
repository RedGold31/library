from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    name: str
    author: str


class BookCreate(BookBase):
    year_of_publication: int | None = None
    genre: str | None = None


class BookUpdate(BaseModel):
    name: str | None = None
    author: str | None = None
    year_of_publication: int | None = None
    genre: str | None = None


class BookResponse(BookCreate):
    id: int
    create_at: datetime
    update_at: datetime
    model_config = ConfigDict(from_attributes=True)
