from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Название приложения
    app_name: str = "FastAPI Shop"
    # Режим отладки - вкл
    debug: bool = True
    # Путь до базы
    database_url: str = "sqlite:///./shop.db"
    # Пути, с которых будут приниматься запросы от фронтенда
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "http://localhost:80",  
        "http://frontend",      
        "http://backend:8000",
    ]
    static_dir: str = "static"
    image_dir: str = "static/images"

    class Config:
        env_file = ".env"


# Инициализируем настройки в переменную
settings = Settings()
