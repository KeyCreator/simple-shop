# Generated by Django 2.2.10 on 2020-06-21 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200621_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя пользователя')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('estimation', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Оценка')),
                ('session_id', models.CharField(max_length=128, verbose_name='Ключ сессии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remarks', to='shop.Product')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы о товарах',
            },
        ),
        migrations.DeleteModel(
            name='Сomment',
        ),
    ]