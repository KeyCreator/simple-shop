# Generated by Django 2.2.10 on 2020-06-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20200621_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remark',
            name='session_id',
            field=models.CharField(max_length=128, unique=True, verbose_name='Ключ сессии'),
        ),
    ]