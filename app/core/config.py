from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_env: str = "local"
    # Provide a sensible default for local/dev so mypy won't complain when
    # creating Settings() at import time in CI. In production this should be
    # provided by env vars or secrets.
    database_url: str = "sqlite+aiosqlite:///:memory:"
    db_schema: str = "public"
    log_level: str = "info"
    port: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env.local",  # local dev; in K8s you use env vars/Secrets instead
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()
