# WSGI Application

"""
WSGI config for zamonaviy_ilmlar project.

This file contains the WSGI configuration required to serve up your web application
as a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zamonaviy_ilmlar.settings')

application = get_wsgi_application()