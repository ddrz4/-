from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class DBConfig(BaseSettings):
    #url
    DB_URL: str

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class AccessToken(BaseSettings):
    lifetime_seconds: int = 3600

    RESET_PASSWORD_TOKEN_SECRET: str
    VERIFICATION_TOKEN_SECRET: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    auth: str = "/auth"
    users: str = "/users"
    messages: str = "/messages"

    @property
    def bearer_token_url(self) -> str:
        # api/v1/auth/login
        parts = (self.prefix, self.auth, "/login")
        path = "".join(parts)
        #return path[1:]
        return path.removeprefix("/")


class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    access_token: AccessToken = AccessToken()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
