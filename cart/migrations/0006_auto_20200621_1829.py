# Generated by Django 2.2.10 on 2020-06-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20200617_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата заказа'),
        ),
    ]
