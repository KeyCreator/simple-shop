import json
import os

from django.core.management.base import BaseCommand

from shop.models import Phone, Clothes, Category, Group
from cart.models import Order
from utils.overriding import slugify


# https://django.fun/tutorials/sozdanie-polzovatelskih-komand-upravleniya-v-django/
class Command(BaseCommand):
    help = u'Загрузка тестовых данных в проект simple-shop'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Загружаемый json-файл')

    def handle(self, *args, **kwargs):
        print('Текущая папка', os.getcwd())

        if Phone.objects.all().count() or \
                Clothes.objects.all().count() or \
                Category.objects.all().count() or \
                Group.objects.all().count() or \
                Order.objects.all().count():
            if input('Существующие записи будут удалены! Нажмите "y" для продолжения:').strip().lower() == 'y':
                Phone.objects.all().delete()
                Clothes.objects.all().delete()
                Category.objects.all().delete()
                Group.objects.all().delete()
                Order.objects.all().delete()
            else:
                return

        print('Данные загружаются')
        path = kwargs['path']
        with open(path, 'r') as file:
            goods = json.load(file, encoding='cp1251')

            phones = goods['Phones']
            clothes = goods['Clothes']

            groups = set(map(lambda foo: foo['group'], phones))
            Group.objects.bulk_create([Group(name=foo) for foo in groups])

            categories = set(map(lambda foo: (foo['category'], foo['group']), phones))
            Category.objects.bulk_create([Category(name=foo[0],
                                                   group=Group.objects.get(name=foo[1]),
                                                   slug=slugify(foo[0]))
                                          for foo in categories])

            for foo in phones:
                Phone.objects.create(article=foo['article'],
                                     name=foo['name'],
                                     price=foo['price'],
                                     description=foo['description'],
                                     image=foo['image'],
                                     category=Category.objects.get(name=foo['category']),
                                     for_main=foo['for_main'])

            for foo in clothes:
                Clothes.objects.create(article=foo['article'],
                                       name=foo['name'],
                                       price=foo['price'],
                                       description=foo['description'],
                                       image=foo['image'])

        print('\nДанные успешно загружены')
