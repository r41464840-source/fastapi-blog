\# FastAPI Blog API



REST API для блога на FastAPI с PostgreSQL, JWT-аутентификацией и миграциями Alembic.



\## Технологии



\- Python и FastAPI

\- PostgreSQL

\- SQLAlchemy

\- Alembic

\- JWT Authentication

\- Gunicorn и Uvicorn

\- Nginx

\- AWS EC2

\- GitHub Actions



\## Возможности



\- Управление постами

\- Регистрация пользователей и аутентификация

\- Категории

\- JWT-токены

\- Миграции базы данных

\- CORS

\- Проверка состояния API и базы данных через `/health`

\- Автоматическое развёртывание через GitHub Actions



\## Запуск локально



1\. Создайте виртуальное окружение:



&#x20;  `python -m venv venv`



2\. Активируйте его в Windows PowerShell:



&#x20;  `.\\venv\\Scripts\\Activate.ps1`



3\. Установите зависимости:



&#x20;  `pip install -r requirements.txt`



4\. Создайте файл `.env` на основе `.env.example` и укажите свои настройки.



5\. Примените миграции:



&#x20;  `alembic upgrade head`



6\. Запустите сервер:



&#x20;  `uvicorn app.main:app --reload`



\## API



\- `/` — главная страница API

\- `/health` — проверка состояния API и подключения к базе данных

\- `/docs` — интерактивная документация, если она включена в конфигурации



\## Deployment



Проект развёрнут на AWS EC2 с использованием Ubuntu, Gunicorn, Uvicorn, systemd и Nginx.



GitHub Actions запускает автоматическое развёртывание при отправке изменений в ветку `main`.



Для автоматического развёртывания используются GitHub Secrets:



\- `EC2\_HOST`

\- `EC2\_USER`

\- `EC2\_SSH\_KEY`



\## Безопасность



Не публикуйте `.env`, пароли базы данных, токены или приватные ключи в GitHub.



\## Лицензия



Учебный проект.

