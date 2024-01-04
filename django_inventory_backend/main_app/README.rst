=====
Inventory Backend
=====

This backend is a Django app meant to be compatible with JavaScript frontends through the help of Django REST.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "main_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'main_app',
    ]

2. Include the main_app URLconf in your project urls.py like this::

    path('items/', include('polls.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an item (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the storefront.