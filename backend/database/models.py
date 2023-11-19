from sqlalchemy import Column, Integer, String

from .config import Base


class Translates(Base):
    __tablename__ = "translates"

    id = Column(Integer, primary_key=True)
    tyvan_word = Column(String, nullable=False)
    russian_word = Column(String, nullable=False)
    telegram_id = Column(Integer, nullable=False)
    telegram_full_name = Column(String, nullable=True)


class PreviousTranslates(Base):
    __tablename__ = "previous_translates"

    id = Column(Integer, primary_key=True)
    row_id = Column(Integer, nullable=True)
    ind = Column(Integer, nullable=True)
    tyv = Column(String, nullable=True)
    ru = Column(String, nullable=True)
    split = Column(String, nullable=True)


class MissingWords(Base):
    __tablename__ = "missing_words"

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
