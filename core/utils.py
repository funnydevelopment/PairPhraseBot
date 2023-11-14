import re


async def is_cyrillic_with_hyphen_string(input_row: str) -> bool:
    pattern = re.compile(r"^[а-яА-ЯӨөҮүҢң-]+$")
    if pattern.match(input_row):
        return True
    return False
