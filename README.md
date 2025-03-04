# Пульт охраны банка

Пульт охраны - это сайт, что работает в  базой данных. Здесь представлены примеры запросов к базе данных: 

1. Получение всех активных пропусков.
2. Получение информации по пропуску человека.
3. Получение информации по активным пользователям.

Запустить данный проект просто так не получится, для работы с ним подребуются [переменные окружения]()

## Зависимости

- Python3.10 должен быть уже установлен. 

[С другими версиями Python, Django3.2.25 не совместим](https://docs.djangoproject.com/en/4.0/faq/install/#what-python-version-can-i-use-with-django)

- Затем используйте `pip` для установки зависимостей:

```pip install -r requirements.txt```

### Переменные окружения

1. Расположите файл `.env` в папку \django_orm_watching_storage_master\project.
2. `.env` должен содержать следующие настройки необходимые для работы базы данных.

Пример содержимого `.env`:
```
DB_ENGINE = db 
DB_HOST = db_host
DB_PORT = db_port
DB_NAME = db_name
DB_USER = db_user
DB_PASSWORD = db_password

DJANGO_SECRET_KEY = bjango_secret_key

DJANGO_DEBUG = django_debug
```
## Запуск

Запустите сайт на локальном сервере командой следующей консольной командой::
```python manage.py runserver 127.0.0.1:8000 ```