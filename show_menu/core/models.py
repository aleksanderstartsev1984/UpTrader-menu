from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class BaseMenu(models.Model):
    name = models.CharField('Название',
                            max_length=settings.CHAR_FIELD_LENGTH,
                            unique=True)
    url = models.CharField('Ссылка',
                           max_length=settings.CHAR_FIELD_LENGTH,
                           unique=True,
                           blank=True,
                           null=True)

    class Meta():
        abstract = True
        ordering = ["pk"]

    def __str__(self):
        return self.name

    def clean(self):
        if hasattr(self, 'parent_menu') and self.url:
            raise ValidationError(
                'Поле "Ссылка" недоступно для редактирования так как'
                f' "{self.name}" имеет наследников:'
                f' "{self.parent_menu.all()}"'
            )


class Menu(BaseMenu):

    class Meta(BaseMenu.Meta):
        verbose_name = 'Меню'
        verbose_name_plural = 'Список доступных меню'


class SubMenuOne(BaseMenu):
    parent = models.ForeignKey(Menu,
                               verbose_name='Меню',
                               related_name='parent_menu',
                               on_delete=models.CASCADE)

    class Meta(BaseMenu.Meta):
        verbose_name = 'Подменю 1'
        verbose_name_plural = 'Список доступных подменю 1'


class SubMenuTwo(BaseMenu):
    parent = models.ForeignKey(SubMenuOne,
                               verbose_name='Подменю 1',
                               related_name='parent_menu',
                               on_delete=models.CASCADE)

    class Meta(BaseMenu.Meta):
        verbose_name = 'Подменю 2'
        verbose_name_plural = 'Список доступных подменю 2'


class SubMenuThree(BaseMenu):
    url = models.CharField('Ссылка',
                           max_length=settings.CHAR_FIELD_LENGTH,
                           unique=True)
    parent = models.ForeignKey(SubMenuTwo,
                               verbose_name='Подменю 2',
                               related_name='parent_menu',
                               on_delete=models.CASCADE)

    class Meta(BaseMenu.Meta):
        verbose_name = 'Подменю 3'
        verbose_name_plural = 'Список доступных подменю 3'
