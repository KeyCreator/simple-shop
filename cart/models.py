from django.db import models


class Cart(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='products')
    count = models.IntegerField(verbose_name='Количество', blank=False, null=False)

    class Meta:
        verbose_name = 'Заказ и товар'
        verbose_name_plural = 'Наполнение заказов'

    def __str__(self):
        return f'{self.product.id} {self.product.name} - {self.count}'


class Order(models.Model):
    pay_date = models.DateField(verbose_name='Дата заказа', auto_now_add=True)
    is_paid = models.BooleanField(verbose_name='Оплачен', default=False)
    user = models.ForeignKey('account.CustomUser',
                             on_delete=models.CASCADE,
                             related_name='orders',
                             blank=True,
                             null=True)

    class Meta:
        verbose_name = 'Заказ покупателя'
        verbose_name_plural = 'Заказы покупателей'

    def __str__(self):
        counts = self.products.all().values('count')
        count = sum(map(lambda foo: foo['count'], counts))
        return '{} : Заказ № {}  от {} , товаров - {}. {}'.format(self.user.username,
                                                                  self.id,
                                                                  self.pay_date,
                                                                  count,
                                                                  "Оплачен" if self.is_paid else "")
