from django.db import models
from django.db.models import PROTECT

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    creation_data = models.DateTimeField(verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Version(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_version = models.IntegerField(verbose_name='Номер версии')
    title_version = models.CharField(max_length=50, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.number_version}'

    class Meta:
        verbose_name = 'Версию'
        verbose_name_plural = 'Версии'
