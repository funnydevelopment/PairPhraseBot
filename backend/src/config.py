from dataclasses import dataclass

from environs import Env


env = Env()
env.read_env(".env")


@dataclass(frozen=True, slots=True)
class Settings:
    user = f'{env.str("DB_USER")}:{env.str("DB_PASS")}'
    database = f'{env.str("DB_HOST")}:{env.str("DB_PORT")}/{env.str("DB_NAME")}'

    db_url = f"postgresql+asyncpg://{user}@{database}"


settings = Settings()
