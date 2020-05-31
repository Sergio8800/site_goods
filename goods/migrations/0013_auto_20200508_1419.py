# Generated by Django 3.0.5 on 2020-05-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0012_auto_20200503_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['-date_post'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ManyToManyField(max_length=100, to='goods.Category'),
        ),
    ]
