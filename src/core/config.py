import functools
import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    root_dir: str = os.path.abspath(__file__ + 3 * "/..")
    src_dir: str = os.path.join(root_dir, "src")

    PROJECT_NAME: str = "/family-tree"

    ENVIRONMENT: str = "local"

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8888

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @functools.cached_property
    def postgres_dsn(self) -> str:
        postgres_host = (
            "localhost" if self.ENVIRONMENT == "local" else self.POSTGRES_HOST
        )
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{postgres_host}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


@functools.lru_cache()
def settings():
    return Settings()
