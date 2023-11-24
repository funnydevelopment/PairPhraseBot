from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import as_declarative

from backend.src.config import settings


engine = create_async_engine(settings.db_url)

async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


@as_declarative()
class Base:
    metadata = MetaData()
