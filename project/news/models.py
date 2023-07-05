from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import gettext as _, gettext_lazy
from django.utils.translation import pgettext_lazy  # импортируем «ленивый» геттекст с подсказкой


class Record(models.Model):  # Класс публикации
    title = models.CharField(verbose_name=gettext_lazy('Название'), max_length=64)
    full_text = models.TextField(verbose_name=gettext_lazy('Статья'))
    data = models.DateTimeField(verbose_name=gettext_lazy('Дата публикации'))
    category = models.ForeignKey('Category', verbose_name=gettext_lazy('Категория'), on_delete=models.CASCADE)

    def preview(self):
        preview = f'{self.full_text[:128]}...'
        return preview

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:                       # Класс для переименования таблицы в админке. Обязательное название класса - Meta
        verbose_name = gettext_lazy('Новость')         # Указываем название таблицы в единственном числе
        verbose_name_plural = gettext_lazy('Новости')  # Указываем название таблицы во множественном числе


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True, help_text=_('category title'))  # добавим переводящийся текст подсказку к полю

    class Meta:
        verbose_name = gettext_lazy('Категория')
        verbose_name_plural = gettext_lazy('Категории')

    def __str__(self):
        return f'{self.title}'


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
