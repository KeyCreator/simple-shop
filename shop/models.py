from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage


NAME_LENGTH = 128
DESCRIPTION_LENGTH = 256
STORAGE = FileSystemStorage(location=settings.MEDIA_ROOT)
ONE, TWO, THREE, FOUR, FIVE = 1, 2, 3, 4, 5
ESTIMATE_CHOICES = [(ONE, '1'), (TWO, '2'), (THREE, '3'), (FOUR, '4'), (FIVE, '5')]


class Product(models.Model):
    article = models.CharField(max_length=NAME_LENGTH, verbose_name='Артикул', unique=True, blank=False, null=False)
    name = models.CharField(max_length=NAME_LENGTH, verbose_name='Модель', blank=False, null=False)
    price = models.FloatField(verbose_name='Цена, руб.', blank=False, null=False)
    description = models.CharField(max_length=DESCRIPTION_LENGTH, verbose_name='Описание', default='')
    image = models.ImageField(upload_to='images', storage=STORAGE)
    orders = models.ManyToManyField('cart.Order',
                                   through='cart.Cart',
                                   through_fields=('product', 'order'),
                                   related_name='goods')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-article']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=NAME_LENGTH, verbose_name='Наименование', unique=True, blank=False, null=False)
    parent = models.ForeignKey('self',
                               verbose_name='Состоит в',
                               on_delete=models.DO_NOTHING,
                               null=True,
                               blank=True,
                               related_name='followers')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Phone(Product):
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name='products')
    for_main = models.BooleanField(verbose_name='Размещать на главной странице', default=False, blank=False, null=False)

    class Meta:
        verbose_name = 'Гаджет'
        verbose_name_plural = 'Смартфоны и аксессуары'
        ordering = ['-article']


class Clothes(Product):

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'


class Remark(models.Model):
    name = models.CharField(verbose_name='Имя пользователя', max_length=NAME_LENGTH, blank=False, null=False)
    content = models.TextField(verbose_name='Содержание', blank=False, null=False)
    estimation = models.IntegerField(verbose_name='Оценка', choices=ESTIMATE_CHOICES, blank=False, null=False)
    session_id = models.CharField(verbose_name='Ключ сессии', max_length=NAME_LENGTH, blank=False, null=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='remarks')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы о товарах'


    def __str__(self):
        return f'{self.product.name} -> {self.name}: {self.estimation}'