from core.models import Menu, SubMenuOne, SubMenuThree, SubMenuTwo
from django.contrib import admin


admin.site.register(Menu)


@admin.register(SubMenuOne)
class SubMenuOneAdmin(admin.ModelAdmin):
    list_filter = ['parent']
    empty_value_display = '-пусто-'

    # disables the ability to select a parent with a non-empty URL field
    def get_form(self, request, obj=None, **kwargs):
        form = super(SubMenuOneAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['parent'].queryset = Menu.objects.filter(url=None)
        return form


@admin.register(SubMenuTwo)
class SubMenuTwoAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = ['parent__parent']
    empty_value_display = '-пусто-'

    # disables the ability to select a parent with a non-empty URL field
    def get_form(self, request, obj=None, **kwargs):
        form = super(SubMenuTwoAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['parent'].queryset = SubMenuOne.objects.filter(
                                                url=None)
        return form


@admin.register(SubMenuThree)
class SubMenuThreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'parent_parent']
    list_filter = ['parent__parent__parent']
    empty_value_display = '-пусто-'

    # disables the ability to select a parent with a non-empty URL field
    def get_form(self, request, obj=None, **kwargs):
        form = super(SubMenuThreeAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['parent'].queryset = SubMenuTwo.objects.filter(
                                                url=None)
        return form

    # information about the parent of the parent in the list display
    def parent_parent(self, obj):
        return obj.parent.parent

    parent_parent.short_description = 'Подменю 1'
