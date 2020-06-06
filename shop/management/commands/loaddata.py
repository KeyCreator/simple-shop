import json
import os

from django.core.management.base import BaseCommand

from shop.models import Product, Category


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Загружаемый json-файл')

    def handle(self, *args, **kwargs):
        print('Текущая папка', os.getcwd())
        print('Данные загружаются')
        path = kwargs['path']
        with open(path, 'r') as file:
            goods = json.load(file, encoding='cp1251')

            Product.objects.all().delete()
            Category.objects.all().delete()

            categories = set(map(lambda foo: foo['category__name'], goods))
            Category.objects.bulk_create([Category(name=foo) for foo in categories])

            Product.objects.bulk_create([Product(article=foo['article'],
                                                 name=foo['name'],
                                                 price=foo['price'],
                                                 image=foo['image'],
                                                 category=Category.objects.get(name=foo['category__name']))
                                         for foo in goods])

        print('\nДанные успешно загружены')