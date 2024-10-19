from typing import (
    TYPE_CHECKING,
    Annotated,
)
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from core.db_helper import DBHelper
from core.models.user import User
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

async def get_user_db(
        session: Annotated[
            "AsyncSession",
            Depends(DBHelper.session_getter),
        ],
    ):
    yield User.get_db(session=session)
