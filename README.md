# show_menu

Test task for the company [UpTrader](https://uptrader.io/)

### Technologies

- Python3
- JavaScript
- CSS
- HTML
- Bash

### Deployment

While in the root folder of the project, run the command
```sh
. project-run
```
This script will create and activate the virtual environment, update the pip
and setuptools packages, install dependencies, create and apply migrations,
create a superuser, create two test menus and a site navigation menu.
The Django server will be launched, accessible at
```
http://127.0.0.1:8000/
```

Tags for test menus and site menus have already been added to the site pages.

To create a new menu, you need to register the necessary items in the site’s
admin panel
```
http://127.0.0.1:8000/admin/
```
The menu is implemented using a template tag.
To add a new menu to a page, you need to place the following code on that page:
```
{% load menu %}
{% addmenu "your menu name" %}
```
Each menu has up to three levels of nesting.
Each menu requires exactly 1 database query to render.

### Author

[Alexander Startsev](https://github.com/aleksanderstartsev1984)
