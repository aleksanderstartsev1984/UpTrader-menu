from core.models import Menu, SubMenuOne, SubMenuThree, SubMenuTwo
from django.contrib import admin


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'url')
    empty_value_display = '-пусто-'


@admin.register(SubMenuOne)
class SubMenuOneAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'url', 'parent')
    empty_value_display = '-пусто-'


@admin.register(SubMenuTwo)
class SubMenuTwoAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'url', 'parent')
    empty_value_display = '-пусто-'


@admin.register(SubMenuThree)
class SubMenuThreeAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'url', 'parent')
    empty_value_display = '-пусто-'
