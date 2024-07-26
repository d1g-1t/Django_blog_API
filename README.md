# Django Blog API

Проект представляет собой API для блога, реализованное с использованием Django и Django REST Framework. API позволяет регистрировать пользователей, создавать, читать, обновлять и удалять статьи и комментарии.

## Стек технологий

- Python 3.x
- Django 3.x
- Django REST Framework
- PostgreSQL
- Simple JWT
- drf-yasg (для документации API)

## Основные функции

- Регистрация пользователей
- Аутентификация с использованием JWT
- CRUD операции для статей
- CRUD операции для комментариев
- Ограничение прав доступа на основе авторства

## Установка и запуск проекта

1. Клонируйте репозиторий:
    ```
    git clone git@github.com:d1g-1t/Django_blog_API.git
    cd Django_blog_API
    ```

2. Создайте и активируйте виртуальное окружение:
    ```
    python -m venv venv
    .\venv\Scripts\activate  # Для Windows
    # source venv/bin/activate  # Для Unix/MacOS
    ```

3. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```

4. Настройте базу данных PostgreSQL и примените миграции:
    ```
    python manage.py migrate
    ```

5. Создайте суперпользователя для доступа к админ-панели:
    ```
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## Использование API

### Регистрация пользователя
- **URL:** `/api/register/`
- **Метод:** `POST`
- **Тело запроса:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```

### Получение токена
- **URL:** `/api/token/`
- **Метод:** `POST`
- **Тело запроса:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```

### CRUD операции для статей
- **URL:** `/api/articles/`
- **Методы:** `GET`, `POST`
- **URL:** `/api/articles/<int:pk>/`
- **Методы:** `GET`, `PUT`, `DELETE`

### CRUD операции для комментариев
- **URL:** `/api/comments/`
- **Методы:** `GET`, `POST`
- **URL:** `/api/comments/<int:pk>/`
- **Методы:** `GET`, `PUT`, `DELETE`
