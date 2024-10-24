from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from core.config import settings


engine = create_async_engine(
    url=settings.db.DB_URL,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

session_factory = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
