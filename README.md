## Описание
В проекте разработано api для сервиса бронирования с базой данных Postgresql.
Реализованы эндпоинты для добавления временного слота без возможности пересечения с уже имеющемся в базе данных, добавление пользователя, удаление пользователя и временного слота по id, вывод всех записей. Написаны тесты на эндпоинты. Проект обернут в docker-compose.
Стэк: Python, FastAPI, psycopg2, pydantic, sqlalchemy, postgresql, pytest, poetry, docker, alembic
## Запуск
```
git clone https://github.com/Vesoore/booking_service.git

cd booking_service

docker-compose up -d
```
