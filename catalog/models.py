from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        pass
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(max_length=150, verbose_name='описание')
    сategory_item = models.CharField(max_length=150, verbose_name='категория')
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        pass
