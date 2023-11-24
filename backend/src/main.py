from fastapi import FastAPI

from backend.src.tgBot.router import router


app = FastAPI()
app.include_router(router=router)
