from typing import TYPE_CHECKING, AsyncGenerator
from fastapi import Depends
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.ext.asyncio import AsyncSession
from .mixins.id_int_pk import IdIntPkMixin
from core.models.mixins.name_str_pk import NameStrPkMixin
from .base import Base
from core.types.user_id import UserIdType
from core.db_helper import session_factory
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class User(Base, IdIntPkMixin, NameStrPkMixin,SQLAlchemyBaseUserTable[UserIdType]):
    pass



async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session


async def get_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
