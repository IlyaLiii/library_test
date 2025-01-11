from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base, str_uniq, int_pk, str_null_true
from datetime import date
from typing import List


# создаем модель таблицы студентов
class Book(Base):
    id: Mapped[int_pk]
    title: Mapped[str]
    description: Mapped[str]
    pub_date: Mapped[date]
    authors: Mapped["Author"] = relationship("Author", back_populates="books")
    genres: Mapped[List[str]]
    count_copy: Mapped[int]

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"title={self.title!r},")

    def __repr__(self):
        return str(self)


class Author(Base):
    id: Mapped[int_pk]
    name: Mapped[str_uniq]
    bio: Mapped[str]
    date_of_birth: Mapped[date]

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)