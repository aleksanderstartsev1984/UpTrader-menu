from django.conf import settings


def insert_view_func(func_name: str):
    """Creates a view function in the file views.py."""
    path_to_insert = f'{settings.BASE_DIR}/app/views.py'
    substring = f"""\n\ndef {func_name}(request):
    name = '{func_name}'
    context = {{'header': name, 'title': name}}
    return render(request, 'app/{func_name}.html', context)\n"""

    with open(path_to_insert, 'r') as f:
        data = f.read()

        if substring in data:
            return

        data = data + substring

    with open(path_to_insert, 'w') as f:
        f.write(data)
