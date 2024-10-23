from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import HTTPBearer
from api.auth import router as auth_router
from api.users import router as users_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    dependencies=[
        Depends(http_bearer),
    ]
)

router.include_router(auth_router)
router.include_router(users_router)


