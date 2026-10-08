from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    algorithm: str
    access_token_expire_minutes: int

    allowed_origins: str = "http://localhost:3000"

    @property
    def origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.allowed_origins.split(",")]

    class Config:
        env_file = ".env"


settings = Settings()