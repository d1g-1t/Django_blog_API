# Django Blog API

Проект представляет собой API для блога, реализованное с использованием Django и Django REST Framework. API позволяет регистрировать пользователей, создавать, читать, обновлять и удалять статьи и комментарии.

## Стек технологий

- Python 3.x
- Django 3.x
- Django REST Framework
- PostgreSQL
- Simple JWT
- drf-yasg (для документации API)

## Локальный запуск проекта

1. Переходим в папку `blog_project/`. Устанавливаем виртуальное окружение на версии Python 3.10+:
    ```sh
    python3.10 -m venv venv
    ```

2. Запускаем виртуальное окружение:
    ```sh
    source venv/Scripts/activate
    ```

3. Обновляем pip, ставим зависимости:
    ```sh
    python -m pip install --upgrade pip && pip install -r requirements.txt
    ```

4. Настраиваем конфигурацию подключения к PostgreSQL. Создаем миграции:
    ```sh
    python manage.py migrate
    ```

5. Запускаем локальный сервер:
    ```sh
    python manage.py runserver
    ```

API проекта: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

Swagger проекта: [http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger)

## Эндпоинты API

### 1. Регистрация пользователя

- **URL:** `http://127.0.0.1:8000/api/register/`
- **Метод:** `POST`
- **Описание:** Регистрирует нового пользователя и возвращает токен.
- **Пример запроса:**
    ```json
    {
      "username": "testuser",
      "password": "testpassword"
    }
    ```
- **Пример ответа:**
    ```json
    {
        "user": {
            "username": "testuser"
        },
        "token": {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjA2ODExMiwiaWF0IjoxNzIxOTgxNzEyLCJqdGkiOiJmZjQxNTM2OWZiNWQ0MTg5OThkZTYwZjJmNThiOWFmMCIsInVzZXJfaWQiOjd9.4kmguWgr6O-ShIeQ9poAY8xYK_InANjOgbXk7AGBmLQ",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxOTgyMDEyLCJpYXQiOjE3MjE5ODE3MTIsImp0aSI6IjNiMWU1OTMzMzZiNDRhMzA5YjdiMmFhODAzZGYwY2MyIiwidXNlcl9pZCI6N30.ZZmNFyAx6Hhd2w3da-l9pE1xG79EfHNJnnqFS2Wuyzk"
        }
    }
    ```

### 2. Берем access-токен

Добавляем в Headers запросов Postman. Отмечаем чекбокс галочкой.

- **key:** `Authorization`
- **value:** `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxOTgyMDEyLCJpYXQiOjE3MjE5ODE3MTIsImp0aSI6IjNiMWU1OTMzMzZiNDRhMzA5YjdiMmFhODAzZGYwY2MyIiwidXNlcl9pZCI6N30.ZZmNFyAx6Hhd2w3da-l9pE1xG79EfHNJnnqFS2Wuyzk`

### 3. Добавление статьи

- **URL:** `http://127.0.0.1:8000/api/articles/`
- **Метод:** `POST`
- **Описание:** Добавляет новую статью в блог.
- **Пример запроса:**
    ```json
    {
      "title": "string",
      "content": "string"
    }
    ```
- **Пример ответа:**
    ```json
    {
        "id": 3,
        "title": "string",
        "content": "string",
        "author": "testuser",
        "created_at": "datetimestamp",
        "updated_at": "datetimestamp"
    }
    ```

### 4. Удаление статьи по id

- **URL:** `http://127.0.0.1:8000/api/articles/{id}/`
- **Метод:** `DELETE`
- **Описание:** Удаляет статью пользователя. Удалить можно только свои статьи.

### 5. Добавление комментария к статье

- **URL:** `http://127.0.0.1:8000/api/comments/`
- **Метод:** `POST`
- **Описание:** Добавляет новую статью в блог.
- **Пример запроса на добавление коммента к статье с id=3:**
    ```json
    {
      "article": 3,
      "content": "string"
    }
    ```
- **Пример ответа:**
    ```json
    {
        "id": 1,
        "article": 3,
        "content": "string",
        "author": "testuser",
        "created_at": "datetimestamp",
        "updated_at": "datetimestamp"
    }
    ```

### 6. Удаление комментария по id

- **URL:** `/api/comments/{id}/`
- **Метод:** `DELETE`
- **Описание:** Удаляет комментарий пользователя. Удалить можно только свои комментарии.

### 7. Создание суперпользователя для доступа к админке

```sh
python manage.py createsuperuser
