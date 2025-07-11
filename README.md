# Инвестиционный портфель

Демонстрационный проект, написанный на Django с использованием чистой архитектуры и DDD

## 🎯 Основные функции

- Создание инвестиционного портфеля
- Отправка приветственного email при создании первого инвестиционного портфеля пользователем
- Добавление в портфель ценных бумаг по тикету (TODO)
- Просмотр стоимости портфеля (TODO)


## 🛠 Технологии

- **Python 3.13+**
- **[Django](https://www.djangoproject.com/)**
- **[Django rest framework](https://www.django-rest-framework.org/)**
- **[Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html) - обработка асинхронных задач**
- **[Dishka](https://github.com/just-work/dishka)** - контейнер внедрения зависимостей
- **[Prometheus](https://prometheus.io/)** - мониторинг метрик (TODO)
- **[Gunicorn](https://gunicorn.org/)** - WSGI-сервер (TODO)
- **[UV](https://github.com/astral-sh/uv)** - менеджер пакетов Python 

## 🏗 Архитектура

Проект построен с использованием следующих архитектурных принципов:

- **Чистая архитектура** - разделение на слои (доменный, прикладной, инфраструктурный)
- **Dependency Injection**
- **Domain-Driven Design**
  - Entities
  - Value objects
  - Domain events
  - Application events
- **REST API**

## 📁 Структура проекта

(TODO)

## 🚀 Запуск проекта

1. Установите зависимости с помощью uv:
```bash
uv pip install .
```

2. Настройте переменные окружения:
```
# Пример конфигурации
SECRET_KEY=your_secret_key # секретный ключ Django
DEBUG=True # запуск в режиме разработки
```

3. Запустите сервер:

Для разработки
```bash
python manage.py runserver
```

gunicorn (TODO)
```bash
```

## 🧪 Тестирование

Запуск тестов (TODO)
```bash
```

## 📊 Мониторинг

Метрики доступны по адресу `/metrics` (Prometheus) (TODO)

## 🔍 Линтеры

В проекте используется [Ruff](https://github.com/astral-sh/ruff)

### Настройка линтера

Конфигурация линтера находится в файле `pyproject.toml` в секции `[tool.ruff]`

### Запуск линтера
```bash
ruff check .
```

Автоматическое исправление проблем
```bash
ruff check --fix .
```

## 🔒 Pre-commit

В проекте настроен pre-commit для автоматической проверки кода перед коммитом. 
Настройки pre-commit находятся в файле `.pre-commit-config.yaml`.

### Установка pre-commit

```bash
pre-commit install
```

После этого pre-commit будет автоматически запускаться перед каждым коммитом.

## 📝 Лицензия
[MIT License](LICENSE)
