from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True,
                             help_text=' Введите номер телефона')
    country = models.CharField(max_length=35, verbose_name='Страна', blank=True, null=True,
                               help_text=' Введите страну')
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name='Аватар', blank=True, null=True,
                               help_text=' Загрузите аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
