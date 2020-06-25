## Проект простого Интернет-магазина
### Инструкция по установке и первому запуску 

Установить зависимости:

```bash
pip install -r requirements.txt
```

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

Запустить веб-сервер проекта:

```bash
python manage.py runserver
```