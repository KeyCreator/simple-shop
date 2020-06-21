import json
import os

from django.core.management.base import BaseCommand

from shop.models import Phone, Clothes, Category


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Загрузка тестовых данных в проект simple-shop'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Загружаемый json-файл')

    def handle(self, *args, **kwargs):
        print('Текущая папка', os.getcwd())
        print('Данные загружаются')
        path = kwargs['path']
        with open(path, 'r') as file:
            goods = json.load(file, encoding='cp1251')

            # Phone.objects.all().delete()
            # Clothes.objects.all().delete()
            # Category.objects.all().delete()

            phones = goods['Phone']
            clothes = goods['Clothes']

            categories = set(map(lambda foo: foo['category__name'], phones))
            Category.objects.bulk_create([Category(name=foo) for foo in categories])

            Phone.objects.bulk_create([Phone(article=foo['article'],
                                             name=foo['name'],
                                             price=foo['price'],
                                             description=foo['description'],
                                             image=foo['image'],
                                             category=Category.objects.get(name=foo['category__name']),
                                             for_main=foo['for_main'])
                                       for foo in phones])

            Clothes.objects.bulk_create([Clothes(article=foo['article'],
                                                 name=foo['name'],
                                                 price=foo['price'],
                                                 description=foo['description'],
                                                 image=foo['image'])
                                         for foo in clothes])

        print('\nДанные успешно загружены')