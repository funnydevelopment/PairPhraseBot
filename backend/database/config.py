from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, as_declarative

from environs import Env

env = Env()
env.read_env(".env")

DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")
DB_USER = env.str("DB_USER")
DB_NAME = env.str("DB_NAME")
DB_PASS = env.str("DB_PASS")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)

async_session_make = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@as_declarative()
class Base:
    metadata = MetaData()
