from django.db import models
from django.conf import settings


NAME_LENGTH = 128


class Product(models.Model):
    article = models.CharField(max_length=NAME_LENGTH, verbose_name='Артикул', unique=True, blank=False, null=False)
    name = models.CharField(max_length=NAME_LENGTH, verbose_name='Модель', blank=False, null=False)
    price = models.FloatField(verbose_name='Цена, руб.', blank=False, null=False)
    image = models.ImageField(upload_to=settings.STATICFILES_DIRS[0])
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=NAME_LENGTH, verbose_name='Наименование', unique=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name