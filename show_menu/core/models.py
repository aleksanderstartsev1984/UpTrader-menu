from django.conf import settings
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

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Menu(BaseMenu):

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Список доступных меню'
        ordering = ["pk"]


class SubMenuOne(BaseMenu):
    parent = models.ForeignKey(Menu,
                               verbose_name='Меню',
                               related_name='parent_menu',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подменю 1'
        verbose_name_plural = 'Список доступных подменю 1'
        ordering = ["pk"]


class SubMenuTwo(BaseMenu):
    parent = models.ForeignKey(SubMenuOne,
                               verbose_name='Подменю 1',
                               related_name='parent_menu',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подменю 2'
        verbose_name_plural = 'Список доступных подменю 2'
        ordering = ["pk"]


class SubMenuThree(BaseMenu):
    url = models.CharField('Ссылка',
                           max_length=settings.CHAR_FIELD_LENGTH)
    parent = models.ForeignKey(SubMenuTwo,
                               verbose_name='Подменю 2',
                               related_name='parent_menu',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подменю 3'
        verbose_name_plural = 'Список доступных подменю 3'
        ordering = ["pk"]
