import random

from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


code = ''.join([str(random.randint(0, 9)) for _ in range(12)])


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='Страна')
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    email_verified = models.BooleanField(default=False, verbose_name='Верификация почты')

    ver_code = models.CharField(max_length=15, default=code, verbose_name='Проверочный код')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
