import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from shop.models import Phone, Clothes, Category, Group


JSON_FILE = 'fixtures.json'


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Создание json-фикстуры из текущей базы данных проекта'

    def handle(self, *args, **kwargs):
        print(self.help)

        phones = []
        for phone in Phone.objects.all().select_related('category'):
            phones.append({'article': phone.article,
                       'name': phone.name,
                       'price': phone.price,
                       'description': phone.description,
                       'image': str(phone.image),
                       'category': phone.category.name,
                       'group': phone.category.group.name,
                       'for_main': phone.for_main})

        clothes = Clothes.objects.all()
        clothes = list(clothes.values('article', 'name', 'price', 'description', 'image'))

        products = {'Phones': phones, 'Clothes': clothes}
        print(products)
        path = os.path.join(settings.BASE_DIR, JSON_FILE)
        with open(path, 'w') as file:
            json.dump(products,
                      file,
                      ensure_ascii=False,
                      indent=2)

        print(f'Файл {JSON_FILE} сформирован в папке проекта')