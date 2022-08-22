from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Приложение QRKot'
    app_description: str = 'Сервис сбора пожертвований для поддержки котиков.'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
