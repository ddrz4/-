from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import (
    Integer,
    ForeignKey,
)
from .base import Base
from core.types.user_id import UserIdType
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from core.models.user import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):  
    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="cascade"),
        nullable=False,
    )


async def get_access_token_db(
    session: AsyncSession = Depends(get_async_session),
):  
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
