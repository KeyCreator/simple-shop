# Generated by Django 3.0.6 on 2020-06-18 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200615_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Product')),
                ('color', models.IntegerField(default=0, verbose_name='Цвет одежды')),
            ],
            options={
                'verbose_name': 'Одежда',
                'verbose_name_plural': 'Одежда',
            },
            bases=('shop.product',),
        ),
    ]
