from email import message
from random import choices
from ssl import create_default_context
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Creator(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='Имя',
        blank=False
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='Фамилия',
        blank=False
    )

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Priority(models.Model):
    priority_value = models.IntegerField(
        null=True,
        default=0,
        validators=[
            MaxValueValidator(
                limit_value=100,
                message='Максимальный приоритет 100',
            ),
            MinValueValidator(
                limit_value=0,
                message='Самый низкий приоритет 0',
            )
        ]
    )
    condition = models.CharField(
        max_length=20,
        verbose_name='Статус задания',
        help_text='Выбери статус задания',
        blank=False,
        default='created',
        choices=settings.CONDITIONS_TYPE
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания задания',
        help_text='Дата присвоена автоматически',
    )
    creators = models.ManyToManyField(
        Creator,
        related_name='creators',
        verbose_name='Исполнители',
    )

    class Meta:
        verbose_name = 'Приоритет заданий'

    def __str__(self):
        return f'{self.priority_value}'
