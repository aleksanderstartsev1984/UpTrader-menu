from django.contrib import admin

from core.models import Menu, SubMenuOne, SubMenuThree, SubMenuTwo


admin.site.register(Menu)


@admin.register(SubMenuOne)
class SubMenuOneAdmin(admin.ModelAdmin):
    list_filter = ['parent']
    empty_value_display = '-пусто-'


@admin.register(SubMenuTwo)
class SubMenuTwoAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = ['parent__parent']
    empty_value_display = '-пусто-'


@admin.register(SubMenuThree)
class SubMenuThreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'parent_parent']
    list_filter = ['parent__parent__parent']
    empty_value_display = '-пусто-'

    def parent_parent(self, obj):
        return obj.parent.parent

    parent_parent.short_description = 'Подменю 1'
