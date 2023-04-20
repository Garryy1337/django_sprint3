from django.db import models


class BaseModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published."""
    """Абстрактная модель. Добавляет Время created_at."""
    is_published = models.BooleanField(
        'Опубликовано',
        default=True, help_text='Снимите галочку, чтобы скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено')

    class Meta:
        abstract = True     