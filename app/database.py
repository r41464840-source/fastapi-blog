from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import settings


# Подключение к PostgreSQL
engine = create_engine(settings.database_url)


# Создание Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Базовый класс для SQLAlchemy моделей
Base = declarative_base()


# Получение DB-сессии
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
