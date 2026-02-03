from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Python Backend API"
    environment: str = "local"

    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"

    jwt_secret_key: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
