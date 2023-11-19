import re


pattern = re.compile(r"^[а-яА-ЯӨөҮүҢң-]+$")


async def is_cyrillic_with_hyphen_string(input_row: str) -> bool:
    return bool(pattern.match(input_row))
