from django.db import models
from core.models import PublishedModel, СreatedModel
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Category(PublishedModel, СreatedModel):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', unique=True, help_text='''
    Идентификатор страницы для URL;
    разрешены символы латиницы, цифры, дефис и подчёркивание.''')
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedModel, СreatedModel):
    name = models.CharField('Название места', max_length=256,)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(PublishedModel, СreatedModel):
    title = models.CharField('Название', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        default=timezone.now,
        help_text='''Если установить дату и время в будущем
         — можно делать отложенные публикации.''')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='публикация',
        null=True,
        blank=True,
        verbose_name='Публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        related_name='местоположение',
        null=True,
        blank=True,
        verbose_name='Местоположения'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='категория',
        verbose_name='Категории',
        null=True,
        blank=True,)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'