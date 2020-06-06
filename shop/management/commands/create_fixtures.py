import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from shop.models import Product, Category


JSON_FILE = 'shop.json'


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Создание json-фикстуры из текущей базы данных проекта'

    def handle(self, *args, **kwargs):
        print(self.help)
        path = os.path.join(settings.BASE_DIR, JSON_FILE)
        products = Product.objects.all().select_related('category')
        products = products.values('article', 'name', 'price', 'image', 'category__name')

        with open(path, 'w') as file:
            json.dump(list(products),
                      file,
                      ensure_ascii=False,
                      indent=2)

        print(f'Файл {JSON_FILE} сформирвоан в папке проекта')