from fastapi import APIRouter


router = APIRouter()


@router.get("/statistic/{telegram_id}")
async def get_user_statistic(telegram_id: int):
    return f"User {telegram_id} statistic: {None}"


@router.post("/add_data")
async def check_and_create_row(translate: str) -> bool:
    pass
