from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base, str_uniq, int_pk, str_null_true
from datetime import date
from typing import List


class User(Base):
    id: Mapped[int_pk]
    name: Mapped[str_uniq]
    is_admin: Mapped[bool]
    email: Mapped[str_uniq]
    password: Mapped[str]
    

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)