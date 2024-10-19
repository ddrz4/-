from typing import (
    TYPE_CHECKING,
    Annotated,
)
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from app.core.db_helper import DBHelper
from app.core.models.user import User
from app.core.models.access_token import AccessToken 
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token_db(
    session: Annotated[
        "AsyncSession",
        Depends(DBHelper.session_getter)
    ],
):  
    yield AccessToken.get_db(session=session)
