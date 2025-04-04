"""
ASGI config for miniproject4JoseSaumat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Sets the default settings for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproject4JoseSaumat.settings')

# Creates the ASGI application instance
application = get_asgi_application()
