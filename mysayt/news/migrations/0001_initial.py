# Generated by Django 4.0.3 on 2022-03-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано?')),
            ],
        ),
    ]
