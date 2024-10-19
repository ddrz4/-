from fastapi import APIRouter
from app.core.config import settings
from .fastapi_users_routers import fastapi_users
from app.api.dependencies.authentication.backend import authentication_backend

router = APIRouter(
    prefix=settings.api.v1.auth
)

router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)
