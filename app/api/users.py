from fastapi import APIRouter
from core.config import settings
from api.fastapi_users_routers import fastapi_users
from core.schemas.user import UserUpdate, UserRead

router = APIRouter(
    prefix=settings.api.users
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
