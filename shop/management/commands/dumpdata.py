import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from shop.models import Phone, Clothes, Category


JSON_FILE = 'fixtures.json'


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Создание json-фикстуры из текущей базы данных проекта'

    def handle(self, *args, **kwargs):
        print(self.help)
        path = os.path.join(settings.BASE_DIR, JSON_FILE)

        phones = Phone.objects.all().select_related('category')
        phones = phones.values('article', 'name', 'price', 'description', 'image', 'category__name', 'for_main')

        clothes = Clothes.objects.all()
        clothes = clothes.values('article', 'name', 'price', 'description', 'image')

        products = {'Phone': list(phones), 'Clothes': list(clothes)}

        with open(path, 'w') as file:
            json.dump(products,
                      file,
                      ensure_ascii=False,
                      indent=2)

        print(f'Файл {JSON_FILE} сформирвоан в папке проекта')