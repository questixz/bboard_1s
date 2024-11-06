from django.db import models


# Create your models here.
class Rubric(models.Model):
    name = models.CharField(
        unique=True,
        max_length=20,
        db_index=True,
        verbose_name='Название',

    )

    def str(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class Bb(models.Model):
    # KINDS = (
    #     ('b', 'Куплю'),
    #     ('s', 'Продам'),
    #     ('c', 'Обменяю'),
    # )

    KINDS = (
        (None, 'Выберите тип публикуемого объявления'),
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю'),
    )

    # KINDS = (
    #     ('Купля-продажа', (
    #         ('b', 'Куплю'),
    #         ('s', 'Продам'),
    #     )),
    #     ('Обмен', (
    #         ('c', 'Обменяю'),
    #     ))
    # )

    kind = models.CharField(
        max_length=1,
        choices=KINDS,
        default='s',
    )
    rubric = models.ForeignKey(
        'Rubric',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика',
    )

    title = models.CharField(
        max_length=50,
        verbose_name='Товар',
    )

    content = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )

    # price = models.FloatField(
    #     null=True,
    #     blank=True,
    #     verbose_name='Цена',
    # )

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        default=0,
        verbose_name='Цена',
    )

    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Опубликовано',
    )

    def str(self):
        return f'{self.title} ({self.price} тг.)'

    class Meta:
        ordering = ['-published', 'title']
        unique_together = ('title', 'published')
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'