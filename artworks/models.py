from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Artwork(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Введите название картины (не более 100 символов).'
    )
    description = models.TextField(
        blank=True,
        verbose_name='О работе',
        help_text='Добавьте описание картины (не обязательно).'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        help_text='Добавьте фотографию картины.'
    )
    completion_date = models.DateField(
        verbose_name='Дата завершения',
        help_text='Добавьте дату завершения работы над картиной.'
    )
    STATUSES = (
        ('sl', 'В продаже'),
        ('sd', 'Продана'),
        ('ns', 'Не продаётся'),
    )
    status = models.CharField(
        max_length=100,
        choices=STATUSES, default='ns',
        verbose_name='Статус',
        help_text='Выбрать статус картины.'
    )
    price = models.IntegerField(
        verbose_name='Цена',
        help_text='Введите цену картины.'
    )


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите текст комментария.'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='artworks',
        verbose_name='Автор комментария',
    )

    class Meta:
        ordering = ('-pub_date',)
