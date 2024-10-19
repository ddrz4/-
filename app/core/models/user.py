from typing import TYPE_CHECKING
from fastapi import Depends
from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy.ext.asyncio import AsyncSession
from .mixins.id_int_pk import IdIntPkMixin
from .base import Base
from app.core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
