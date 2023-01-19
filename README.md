# Yatube API

REST API для проекта [Yatube](https://github.com/ivr42/yatube)

(Yatube — концепт социальной сети для публикации дневников.)

## Стек технологий, использованных в проекте
- Python 3.7
- Django 2.2
- Django REST Framework (DRF)
- SimpleJWT
- SQLite


## Как установить проект:
1. Клонировать репозиторий и перейти в него в командной строке:
```shell
git clone https://github.com/ivr42/yatube_api
```
```shell
cd yatube_api
```

2. Cоздать и активировать виртуальное окружение:
```shell
python3 -m venv venv
```
```shell
source venv/bin/activate
```

3. Установить зависимости из файла requirements.txt:
```shell
python3 -m pip install --upgrade pip
```
```shell
pip install -r requirements.txt
```

4. Выполнить миграции:
```shell
python3 manage.py migrate
```
## Как запустить проект:
```shell
python3 manage.py runserver
```

## Описание API проекта Yatube (v1)

### Получение публикаций `GET /api/v1/posts/`
Получить список всех публикаций. При указании параметров `limit` и `offset` 
выдача должна работать с пагинацией.

#### Пример ответа:
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Создание новой публикации `POST /api/v1/posts/`
Добавление новой публикации в коллекцию публикаций.
Анонимные запросы запрещены.

#### Пример запроса:
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
#### Пример ответа:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Получение публикации `GET /api/v1/posts/{id}/`
Получение публикации по id.

#### Пример ответа:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Обновление публикации `PUT /api/v1/posts/{id}/`
Обновление публикации по id.
Обновить публикацию может только автор публикации.
Анонимные запросы запрещены.

#### Пример запроса:
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
#### Пример ответа:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Частичное обновление публикации `PATCH /api/v1/posts/{id}/`
Частичное обновление публикации по id.
Обновить публикацию может только автор публикации.
Анонимные запросы запрещены.

#### Пример запроса:
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
#### Пример ответа:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Частичное обновление публикации `DELETE /api/v1/posts/{id}/`
Удаление публикации по id.
Удалить публикацию может только автор публикации.
Анонимные запросы запрещены.

### Получение комментариев `GET /api/v1/posts/{post_id}/comments/`
Получение всех комментариев к публикации.

#### Пример ответа:
```json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

### Добавление комментария `POST /api/v1/posts/{post_id}/comments/`
Добавление нового комментария к публикации. Анонимные запросы запрещены.

#### Пример запроса:
```json
{
  "text": "string"
}
```
#### Пример ответа:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
### Получение комментария `GET /api/v1/posts/{post_id}/comments/{id}/`
Получение комментария к публикации по id.

#### Пример ответа:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Обновление комментария `PUT /api/v1/posts/{post_id}/comments/{id}/`
Обновление комментария к публикации по id.
Обновить комментарий может только автор комментария.
Анонимные запросы запрещены.

#### Пример запроса:
```json
{
  "text": "string"
}
```
#### Пример ответа:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Частичное обновление комментария `PATCH /api/v1/posts/{post_id}/comments/{id}/`
Частичное обновление комментария к публикации по id.
Обновить комментарий может только автор комментария.
Анонимные запросы запрещены.

#### Пример запроса:
```json
{
  "text": "string"
}
```
#### Пример ответа:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Список сообществ `GET /api/v1/groups/`
Получение списка доступных сообществ.

#### Пример ответа:
```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

### Информация о сообществе `GET /api/v1/groups/{id}/`
Получение информации о сообществе по id.

#### Пример ответа:
```json
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```

### Подписки `GET /api/v1/follow/`
Возвращает все подписки пользователя, сделавшего запрос.
Анонимные запросы запрещены.

#### Пример ответа:
```json
[
  {
    "user": "string",
    "following": "string"
  }
]
```

### Подписка `PUT /api/v1/follow/`
Подписка пользователя от имени которого сделан запрос на пользователя
переданного в теле запроса. Анонимные запросы запрещены.

#### Пример запроса:
```json
{
  "following": "string"
}
```
#### Пример ответа:
```json
{
  "user": "string",
  "following": "string"
}
```

### Получить JWT-токен `POST /api/v1/jwt/create/`
Получение JWT-токена.

#### Пример запроса:
```json
{
  "username": "string",
  "password": "string"
}
```
#### Пример ответа:
```json
{
  "refresh": "string",
  "access": "string"
}
```

### Обновить JWT-токен `POST /api/v1/jwt/refresh/`

#### Пример запроса:
```json
{
  "refresh": "string"
}
```
#### Пример ответа:
```json
{
  "access": "string"
}
```

### Проверить JWT-токен `POST /api/v1/jwt/verify/`
Проверка JWT-токена.

#### Пример запроса:
```json
{
  "token": "string"
}
```
