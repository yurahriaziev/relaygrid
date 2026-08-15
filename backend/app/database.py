from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config import settings

from collections.abc import AsyncGenerator

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session