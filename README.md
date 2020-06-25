## Проект простого Интернет-магазина
### Инструкция по установке и первому запуску 


Провести миграцию:

```bash
python manage.py makemigrations
python manage.py migrate
```

Загрузить тестовые данные:

```bash
python manage.py loaddata fixtures.json
```

Создать тестового суперпользователя:

```bash
python manage.py createsuperuser
```

Запустить  веб-сервер проекта:

```bash
python manage.py runserver
```