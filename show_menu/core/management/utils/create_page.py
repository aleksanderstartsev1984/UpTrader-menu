import os
from django.conf import settings


def insert_page(page_name: str):
    """Creates an HTML document(website page)."""
    path_to_copy = f'{settings.TEMPLATES_DIR}/app/index.html'
    path_to_insert = f'{settings.TEMPLATES_DIR}/app/{page_name}.html'

    if os.path.isfile(path_to_insert):
        return

    with open(path_to_copy, 'r') as f:
        data = f.read()

    with open(path_to_insert, 'w') as f:
        f.write(data)
