# API Autotests

Набор автотестов для публичного REST API [JSONPlaceholder](https://jsonplaceholder.typicode.com).

Стек: **Python, pytest, requests**

## Что проверяется
- Статус-коды (`200`, `201`, `404`)
- Структура ответов (`/posts`, `/users`, `/comments`, `/todos`)
- CRUD: `POST`, `PUT`, `PATCH`, `DELETE`
- Негативные сценарии: несуществующий id, неверный тип id, неверный роут
- `Content-Type: application/json` и время ответа < 2.5с

## Запуск

```bash
pip install -r requirements.txt
pytest -v
```

Всего 14 тестов, внешний API-ключ не нужен.
