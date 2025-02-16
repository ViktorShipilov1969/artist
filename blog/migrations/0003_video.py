# Generated by Django 3.2.20 on 2023-11-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20231118_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название видео.', max_length=200, verbose_name='Название видео')),
                ('description', models.TextField(blank=True, help_text='Добавьте описание видео (не обязательно).', verbose_name='Описание')),
                ('link', models.TextField(help_text='Добавьте ссылку из Ютуба.', verbose_name='Ссылка')),
            ],
        ),
    ]
