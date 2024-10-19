from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class DBConfig(BaseModel):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def db_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    model_config = SettingsConfigDict(env_file=".env")


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    RESET_PASSWORD_TOKEN_SECRET: str
    VEREFICATION_TOKEN_SECRET: str

    model_config = SettingsConfigDict(env_file=".env")


class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    access_token: AccessToken = AccessToken()


settings = Settings()