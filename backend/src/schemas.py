from pydantic import BaseModel


class UserTranslate(BaseModel):
    id: int
    tyvan_word: str
    russian_word: str
    telegram_id: int
    telegram_full_name: str

    class Config:
        from_attributes = True
