from fastapi_users import schemas
from core.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    name: str


class UserCreate(schemas.BaseUserCreate):
    name: str


class UserUpdate(schemas.BaseUserUpdate):
    name: str
