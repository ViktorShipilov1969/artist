# Generated by Django 3.2.20 on 2023-12-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20231207_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='link_code',
            field=models.TextField(help_text='Добавьте код из Ютуба.', verbose_name='Код для вставки видео'),
        ),
        migrations.AlterField(
            model_name='video',
            name='link_youtube',
            field=models.TextField(help_text='Добавьте ссылку на видео.', verbose_name='Ссылка'),
        ),
    ]
