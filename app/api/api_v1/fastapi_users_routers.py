from fastapi_users import FastAPIUsers
from app.core.types.user_id import UserIdType
from app.core.models.user import User
from app.api.dependencies.authentication.backend import authentication_backend
from ..dependencies.authentication.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
