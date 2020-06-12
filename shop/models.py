from django.db import models
from django.conf import settings

from account.models import CustomUser


NAME_LENGTH = 128
DESCRIPTION_LENGTH = 256


class Product(models.Model):
    article = models.CharField(max_length=NAME_LENGTH, verbose_name='Артикул', unique=True, blank=False, null=False)
    name = models.CharField(max_length=NAME_LENGTH, verbose_name='Модель', blank=False, null=False)
    price = models.FloatField(verbose_name='Цена, руб.', blank=False, null=False)
    description = models.CharField(max_length=DESCRIPTION_LENGTH, verbose_name='Описание', default='')
    image = models.ImageField(upload_to=settings.STATICFILES_DIRS[0])
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name='products')
    for_main = models.BooleanField(verbose_name='Размещать на главной странице', default=False, blank=False, null=False)
    users = models.ManyToManyField('account.CustomUser',
                                   through='Cart',
                                   through_fields=('product', 'user'),
                                   related_name='buyers')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='purchases')
    count = models.IntegerField(verbose_name='Количество', blank=False, null=False)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Корзины покупателей'

    def __str__(self):
        return f'{self.user.email} {self.product.name} - {self.count}'


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
