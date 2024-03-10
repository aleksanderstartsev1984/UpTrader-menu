from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from core.management.commands.create_menu import Command
from core.models import Menu


PATH_TO_SIDEBAR = settings.TEMPLATES_DIR + '/includes/sidebar.html'


def index(request):
    name = 'home'
    context = {'header': name, 'title': name}
    return render(request, 'app/index.html', context)


def create_menu(request):
    add_menu = Command()
    name = add_menu.handle()
    substring = '<div id="include-test-menu"></div>'
    with open(PATH_TO_SIDEBAR, 'r') as f:
        data = f.read()
        data = data.replace(substring,
                            '{% addmenu "' + name + '" %}\n' + substring)
    with open(PATH_TO_SIDEBAR, 'w') as f:
        f.write(data)

    return redirect(request.META.get('HTTP_REFERER'))


def delete_menu(request):
    menu = Menu.objects.last()
    if not menu or menu.id == 1:
        messages.add_message(request,
                             messages.ERROR,
                             "Нет доступных для удаления элементов.")
    else:
        menu.delete()
        with open(PATH_TO_SIDEBAR, 'r') as f:
            data = f.read()
            data = data.replace('{% addmenu "' + menu.name + '" %}\n', '')
        with open(PATH_TO_SIDEBAR, 'w') as f:
            f.write(data)

    return redirect(request.META.get('HTTP_REFERER'))
