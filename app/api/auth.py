from fastapi import APIRouter
from core.config import settings
from api.fastapi_users_routers import fastapi_users
from api.dependencies.authentication.backend import authentication_backend
from core.schemas.user import UserCreate, UserRead

router = APIRouter(
    prefix=settings.api.auth
)

# login & logout
router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)

# register
router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
)
