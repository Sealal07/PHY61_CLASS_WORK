import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = "sqlite+aiosqlite:///test.db"
# 1. Создание ассинхроного движка
engine = create_async_engine(DATABASE_URL, echo=True)

# 2. Создание фабрики сессий
async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 3. Вспомогательная функция для получении\ сессии
async def get_async_session():
    async with async_session_maker() as session:
        yield session

