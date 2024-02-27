from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import Menu, SubMenuOne, SubMenuThree, SubMenuTwo


MAIN_MENU_NAME = 'Test menu'
SUB_MENU_NAME = 'Sub menu'


class Command(BaseCommand):
    """Create test menu."""

    def handle(self, *args, **options):
        try:
            menu = Menu.objects.create(name=MAIN_MENU_NAME)
            menu.name += ' ' + str(menu.id)
            menu.save()
            menu_id = menu.id
            self.stdout.write(
                self.style.SUCCESS(f'CREATION MENU <{menu.name}> OK')
            )

            data_points_1 = []
            for point in range(1, settings.NUMBER_OF_ITEMS + 1):
                sub_menu_1_name = f'{SUB_MENU_NAME}.{menu_id}.{point}'
                parent = Menu.objects.get(pk=menu_id)
                data_points_1.append(SubMenuOne(
                    name=sub_menu_1_name, parent=parent
                ))
            SubMenuOne.objects.bulk_create(data_points_1)
            self.stdout.write(
                self.style.SUCCESS(f'CREATION MENU <{SUB_MENU_NAME} 1> OK')
            )

            data_points_2 = []
            for parent_point in data_points_1:
                for point in range(1, settings.NUMBER_OF_ITEMS + 1):
                    sub_menu_2_name = (
                        f'{parent_point.name}.{point}'
                    )
                    parent = parent_point
                    data_points_2.append(SubMenuTwo(
                        name=sub_menu_2_name, parent=parent
                    ))
            SubMenuTwo.objects.bulk_create(data_points_2)
            self.stdout.write(
                self.style.SUCCESS(f'CREATION MENU <{SUB_MENU_NAME} 2> OK')
            )

            data_points_3 = []
            count = 0
            for parent_point in data_points_2:
                for point in range(1, settings.NUMBER_OF_ITEMS + 1):
                    count += 1
                    sub_menu_3_name = (
                        f'{parent_point.name}.{point}'
                    )
                    data_points_3.append(SubMenuThree(
                        name=sub_menu_3_name,
                        url=f'{menu_id}.{count}',
                        parent=parent_point
                    ))
            SubMenuThree.objects.bulk_create(data_points_3)
            self.stdout.write(
                self.style.SUCCESS(f'CREATION MENU <{SUB_MENU_NAME} 3> OK')
            )

        except Exception as error:
            self.stdout.write(
                self.style.ERROR(f'CREATION MENU ERROR: {error}')
            )
