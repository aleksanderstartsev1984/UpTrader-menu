from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import Menu, SubMenuOne, SubMenuTwo


MAIN_MENU_NAME = 'Menu'
SUB_MENU_NAME = 'pages site'
S_SUB_MENU_NAME = 'page'
URL = 'http://127.0.0.1:8000/page'


class Command(BaseCommand):
    """Creating a site menu."""

    def handle(self, *args, **options):
        try:
            menu = Menu.objects.create(name=MAIN_MENU_NAME)
            self.stdout.write(
                self.style.SUCCESS(f'CREATION MENU <{MAIN_MENU_NAME}> OK')
            )

            sub_menu = SubMenuOne.objects.create(name=SUB_MENU_NAME,
                                                 parent=menu)
            self.stdout.write(
                self.style.SUCCESS(f'CREATION MENU <{SUB_MENU_NAME}> OK')
            )

            data_points = []
            data_points.append(SubMenuTwo(
                name='home',
                url='http://127.0.0.1:8000/',
                parent=sub_menu
            ))
            for point in range(1, settings.NUMBER_OF_ITEMS_SITE + 1):
                sub_menu_2_name = f'{S_SUB_MENU_NAME}{point}'
                url = f'{URL}{point}'
                parent = sub_menu
                data_points.append(SubMenuTwo(
                    name=sub_menu_2_name, url=url, parent=parent
                ))
            SubMenuTwo.objects.bulk_create(data_points)
            self.stdout.write(
                self.style.SUCCESS(f'CREATION MENU <{S_SUB_MENU_NAME}> OK')
            )

        except Exception as error:
            self.stdout.write(
                self.style.ERROR(f'CREATION MENU ERROR: {error}')
            )
