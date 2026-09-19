from datetime import datetime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    year_of_publication: Mapped[int | None] = mapped_column()
    genre: Mapped[str | None] = mapped_column()
    create_at: Mapped[datetime] = mapped_column(nullable=False)
    update_at: Mapped[datetime] = mapped_column(nullable=False)
