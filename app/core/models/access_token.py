from datetime import datetime
from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import (
    Integer,
    ForeignKey,
    String,
)
from .base import Base
from core.types.user_id import UserIdType
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from core.models.user import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users_db_sqlalchemy.generics import TIMESTAMPAware, now_utc


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    token: Mapped[str] = mapped_column(
        String(length=43),
        primary_key=True,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
            TIMESTAMPAware(timezone=True),
            nullable=False,
            default=now_utc
        )
    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="cascade"),
        nullable=False
    )


async def get_access_token_db(
    session: AsyncSession = Depends(get_async_session),
):  
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
