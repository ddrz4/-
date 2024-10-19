from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class DBConfig(BaseSettings):
    DB_URL: str
    
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    model_config = SettingsConfigDict(env_file=".env")


class AccessToken(BaseSettings):
    lifetime_seconds: int = 3600
    RESET_PASSWORD_TOKEN_SECRET: str
    VEREFICATION_TOKEN_SECRET: str

    model_config = SettingsConfigDict(env_file=".env")


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"
    messages: str = "/messages"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    access_token: AccessToken = AccessToken()
    api: ApiPrefix = ApiPrefix()


settings = Settings()