from typing import (
    TYPE_CHECKING,
    Annotated,
)
from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from core.models.access_token import AccessToken
from core.config import settings
from core.models.access_token import get_access_token_db
if TYPE_CHECKING:
    from app.core.models.access_token import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase

def get_database_strategy(
    access_tokens_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(get_access_token_db),
    ]
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_tokens_db,
        lifetime_seconds=settings.access_token.lifetime_seconds
    )
