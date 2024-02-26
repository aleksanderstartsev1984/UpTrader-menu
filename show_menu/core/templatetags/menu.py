from core.models import Menu
from django.template import Library

register = Library()


@register.inclusion_tag('core/menu.html')
def addmenu(name_menu: str) -> dict:
    """Disassembles a set of requests for menu options."""

    full_menu = Menu.objects.filter(name=name_menu).values_list(
        # core.models.Menu
        'name', 'url',

        # core.models.SubMenuOne
        'parent_menu__name',
        'parent_menu__url',
        'parent_menu__parent__name',

        # core.models.SubMenuTwo
        'parent_menu__parent_menu__name',
        'parent_menu__parent_menu__url',
        'parent_menu__parent_menu__parent__name',

        # core.models.SubMenuThree
        'parent_menu__parent_menu__parent_menu__name',
        'parent_menu__parent_menu__parent_menu__url',
        'parent_menu__parent_menu__parent_menu__parent__name',
    )

    main_menu = {}
    sub_menu_one, sub_menu_two, sub_menu_three = [], [], []
    name = 'name'
    url = 'url'
    parent = 'parent'
    for i in full_menu:
        if not main_menu:
            main_menu = {name: i[0], url: i[1]}
        s_m_1 = {name: i[2], url: i[3], parent: i[4]}
        s_m_2 = {name: i[5], url: i[6], parent: i[7]}
        s_m_3 = {name: i[8], url: i[9], parent: i[10]}

        if s_m_1 not in sub_menu_one and s_m_1.get(name) is not None:
            sub_menu_one.append(s_m_1)
        if s_m_2 not in sub_menu_two and s_m_2.get(name) is not None:
            sub_menu_two.append(s_m_2)
        if s_m_3 not in sub_menu_three and s_m_3.get(name) is not None:
            sub_menu_three.append(s_m_3)

    data_context = {
        'main_menu': main_menu,
        'sub_menu_one': sub_menu_one,
        'sub_menu_two': sub_menu_two,
        'sub_menu_three': sub_menu_three,
    }

    return data_context
