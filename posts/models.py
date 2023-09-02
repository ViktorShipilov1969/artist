from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название поста',
        help_text='Введите название поста.'
    )
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст публикации.'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ('-pub_date',)


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
        related_name='posts',
        verbose_name='Автор комментария',
    )

    class Meta:
        ordering = ('-pub_date',)
