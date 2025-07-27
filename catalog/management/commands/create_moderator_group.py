# products/management/commands/create_moderator_group.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" и назначает ей права'

    def handle(self, *args, **options):
        try:
            moderators_group, created = Group.objects.get_or_create(name="Модератор продуктов")

            # Получаем ContentType для модели Product
            product_content_type = ContentType.objects.get_for_model(Product)

            # Получаем разрешение на изменение продукта (change_product)

            change_product_permission = Permission.objects.get(
                codename='change_product',
                content_type=product_content_type
            )

            # Получаем разрешение на удаление
            delete_product_permission = Permission.objects.get(
                codename='delete_product',
                content_type=product_content_type
            )

            # Получаем кастомное разрешение на отмену публикации
            can_unpublish_permission = Permission.objects.get(
                codename='can_unpublish_product',
                content_type=product_content_type
            )

            # Добавляем разрешения в группу
            moderators_group.permissions.add(delete_product_permission, can_unpublish_permission,
                                             change_product_permission)

            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана и права назначены.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Ошибка при создании группы: {e}'))
