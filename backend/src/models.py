from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database import Base


class Translates(Base):
    __tablename__ = "translates"

    id: Mapped[int] = mapped_column(primary_key=True)
    tyvan_word: Mapped[str] = mapped_column(nullable=False)
    russian_word: Mapped[str] = mapped_column(nullable=False)
    telegram_id: Mapped[int] = mapped_column(nullable=False)
    telegram_full_name: Mapped[str] = mapped_column(nullable=True)


class PreviousTranslates(Base):
    __tablename__ = "previous_translates"

    id: Mapped[int] = mapped_column(primary_key=True)
    row_id: Mapped[str] = mapped_column(nullable=True)
    ind: Mapped[str] = mapped_column(nullable=True)
    tyv: Mapped[str] = mapped_column(nullable=True)
    ru: Mapped[str] = mapped_column(nullable=True)
    split: Mapped[str] = mapped_column(nullable=True)


class MissingWords(Base):
    __tablename__ = "missing_words"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(nullable=False)
