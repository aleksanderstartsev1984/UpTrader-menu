from django.contrib import messages
from django.shortcuts import redirect, render

from core.management.commands.create_menu import Command
from core.models import Menu


def index(request):
    name = 'home'
    context = {'header': name, 'title': name}
    return render(request, 'app/index.html', context)


def create_test_menu(request):
    add_menu = Command()
    name = add_menu.handle()
    with open('./templates/base.html', 'r') as f:
        data = f.read()
        data = data.replace('<div id="include"></div>',
                            '{% addmenu "' + name + '" %}\n'
                            '<div id="include"></div>')
    with open('./templates/base.html', 'w') as f:
        f.write(data)

    return redirect(request.META.get('HTTP_REFERER'))


def delete_test_menu(request):
    menu = Menu.objects.last()
    if not menu or menu.id < 2:
        messages.add_message(request,
                             messages.ERROR,
                             "Нет доступных для удаления элементов.")
    else:
        menu.delete()
        with open('./templates/base.html', 'r') as f:
            data = f.read()
            data = data.replace('{% addmenu "' + menu.name + '" %}\n', '')
        with open('./templates/base.html', 'w') as f:
            f.write(data)

    return redirect(request.META.get('HTTP_REFERER'))
