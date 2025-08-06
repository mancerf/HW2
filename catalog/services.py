from config.settings import CACHES_ENABLED
from catalog.models import Product, Category
from django.core.cache import cache


def get_products_by_category(category_name):
    try:
        category = Category.objects.get(name=category_name)
        return Product.objects.filter(category=category)
    except Category.DoesNotExist:
        return []


def get_product_from_cache(category_name=None):
    if not CACHES_ENABLED:
        if category_name:
            return Product.objects.filter(category__name=category_name, price__gt=0).order_by('price')
        return Product.objects.filter(price__gt=0).order_by('price')

    # Формируем разные ключи кеша для разных категорий
    key = f'Product_List_{category_name}' if category_name else 'All_Products'

    products = cache.get(key)
    if products is not None:
        return products

    # Выполняем фильтрацию товаров по категории, если она указана
    if category_name:
        products = Product.objects.filter(category__name=category_name, price__gt=0).order_by('price')
    else:
        products = Product.objects.filter(price__gt=0).order_by('price')

    cache.set(key, products)
    return products
