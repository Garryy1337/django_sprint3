from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published."""
    is_published = models.BooleanField(
        'Опубликовано',
        default=True, help_text='Снимите галочку, чтобы скрыть публикацию.')

    class Meta:
        abstract = True


class СreatedModel(models.Model):
    """Абстрактная модель. Добавляет Время created_at."""
    created_at = models.DateTimeField('Добавлено')
     
    class Meta:
        abstract = True        