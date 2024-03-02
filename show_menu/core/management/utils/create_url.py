from django.conf import settings


def insert_path(view_func_name: str):
    """Creates an url path in urls.py."""
    path_to_insert = f'{settings.BASE_DIR}/app/urls.py'
    substring = (f"    path('{view_func_name}',"
                 f" views.{view_func_name},"
                 f" name='{view_func_name}'),")

    with open(path_to_insert, 'r') as f:
        data = f.read()

        if substring in data:
            return

        data = data.replace(']', substring + '\n]')

    with open(path_to_insert, 'w') as f:
        f.write(data)
