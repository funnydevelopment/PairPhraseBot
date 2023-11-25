import os

import aiohttp


class TranslateClient:
    api_server = os.getenv("SERVER")

    async def get_user_stat(self, telegram_id: int):
        async with aiohttp.ClientSession() as session:
            url = f"{self.api_server}/statistic/{telegram_id}"
            async with session.get(url=url) as response:
                return await response.text()

    async def add_translate_data(self, telegram_id: int, tuv: str, ru: str):
        async with aiohttp.ClientSession() as session:
            url = f"{self.api_server}/add_data"
            params = {
                "telegram_id": telegram_id,
                "tuv": tuv,
                "ru": ru
            }
            async with session.post(url=url, data=params) as response:
                return await response.text()
