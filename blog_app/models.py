from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    '''Модель статьи'''
    title = models.CharField(
        'Название статьи',
        max_length=255
    )
    content = models.TextField(
        'Содержание статьи',
        max_length=10000
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Comment(models.Model):
    '''Модель комментария'''
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Статья'
    )
    content = models.TextField(
        'Содержание комментария',
        max_length=1000
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )

    def __str__(self):
        return f'Комментарий от {self.author} к {self.article}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']
