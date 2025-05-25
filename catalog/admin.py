from django.contrib import admin

# Register your models here.
from .models import Category, Product



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'сategory_item')
    list_filter = ('сategory_item',)
    search_fields = ('name','description')