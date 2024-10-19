from typing import TYPE_CHECKING
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.ext.asyncio import AsyncSession
from .mixins.id_int_pk import IdIntPkMixin
from .base import Base
from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
