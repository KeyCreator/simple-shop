# Generated by Django 2.2.10 on 2020-06-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20200621_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remark',
            name='session_id',
            field=models.CharField(max_length=128, verbose_name='Ключ сессии'),
        ),
    ]
