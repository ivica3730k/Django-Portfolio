"""
WSGI config for portfolioWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
#sys.path.append(put path to django project root here)
#sys.path.append(put path to python environment here,can be venv , i.e. ../venv/lib/python3.6/site-packages)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolioWeb.settings')

application = get_wsgi_application()
