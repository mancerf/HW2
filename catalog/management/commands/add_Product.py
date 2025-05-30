from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test Product to the database'
    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **kwargs):
        group, _ = Category.objects.get_or_create(name='животные')

        products = [
            {'name' = 'тигр', 'description' = 'рыжий', 'сategory_item' = 'животное', 'price' = '100'},
            {'name' = 'лось', 'description' = 'рогатый', 'сategory_item' = 'животное','price' = '1000'},
            {'name' = 'машина', 'description' = 'красная', 'сategory_item' = 'машина','price' = '100000'}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {Product.name} {Product.сategory_item}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'product already exists: {Product.name} {Product.сategory_item}'))