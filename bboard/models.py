from django.core import validators
from django.db import models
from django.core.exceptions import ValidationError

def validate_even(val):
    if val % 2 !=0:
     raise ValidationError('Число %(value)s нечетное', code='odd',
                          params={'value: val'})

class MinMaxValueValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max>max_value

    def __call__(self, val):
        if val < self.min_value or val > self.max_value:
            raise ValidationError('введеное число должно' 'находиться в диапозоне от %(min)s до %(max)s',
                                  code='out_of_range',
                                  params={'value: val'})


class Rubric(models.Model):
    name = models.CharField(
        unique=True,
        max_length=20,
        db_index=True,
        verbose_name='Название',

    )



    def __str__(self):
         return f'{self.name}'

    # def get_absolute_url(self):
    #   return f"{self.pk}/"

    # def save(self, *args, **kwargs):
    #     super().save(*args,**kwargs)
    #
    # def delete(self, *args, **kwargs):
    #     super().delete(*args, **kwargs)

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

    new_file = models.CharField(
         max_length=50,
         null=True,
         blank=True,
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
        validators=[validators.RegexValidator(regex='^.{4,}$')],
        error_messages={'invalid':'введите 4 и более символов'},
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
        validators=[validate_even]
    )

    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Опубликовано',
    )

    def title_and_price(self):
        if self.price:
            return f'{self.title} ({self.price:.2f} тг.)'
        return self.title

    title_and_price.short_description = 'Название и цена'

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите описание товара')
        if self.price and self.price < 0:
            errors['price'] = ValidationError('Укажите не отрицат знач цены')
        if errors:
            raise ValidationError(errors)
    def __str__(self):
        return f'{self.title} ({self.price} тг.)'

    class Meta:
        ordering = ['-published', 'title']
        unique_together = ('title', 'published')
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


