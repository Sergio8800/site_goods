# Generated by Django 3.0.5 on 2020-05-03 08:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20200428_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['name'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='reviews',
            name='date_post',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата сообщения'),
            preserve_default=False,
        ),
    ]
