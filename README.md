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
. project-run.sh
```
This script will create and activate the virtual environment, update the pip
and setuptools packages, install dependencies, create and apply migrations,
create a superuser, create one menu site navigation.

The Django server will be launched, accessible at
```
http://127.0.0.1:8000/
```

Tag for site menus have already been added to the base template.
To quickly create a new menu, the “add menu” button has been implemented,
to delete the last created menu, click on the “delete last menu” button.

To create a new menu, you need to register the necessary items in the site’s admin panel
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

### Latest version

The latest version is in the dev branch.

### Author

[Alexander Startsev](https://github.com/aleksanderstartsev1984)
