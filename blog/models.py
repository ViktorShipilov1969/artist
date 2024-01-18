from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название поста',
        help_text='Введите название поста.'
    )
    subtitle = models.CharField(
        max_length=500,
        verbose_name='Подзаголовок',
        help_text='Введите подзаголовок поста.',
        blank=True
    )
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст публикации.'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    cover = models.ImageField(
        verbose_name='Обложка статьи',
        help_text='Добавьте фотографию картины.',
        blank=True
    )

    class Meta:
        ordering = ('-pub_date',)


class Video(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название видео',
        help_text='Введите название видео.'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        help_text='Добавьте описание видео (не обязательно).'
    )
    link_code = models.TextField(
        verbose_name='Код для вставки видео',
        help_text='Добавьте код из Ютуба.'
    )
    link_youtube = models.TextField(
        verbose_name='Ссылка',
        help_text='Добавьте ссылку на видео.'
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
        related_name='comments',
        verbose_name='Автор комментария',
        default=None,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
        default=None,
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return 'Комментарий {} от пользователя {}'.format(
            self.text, self.author
            )
