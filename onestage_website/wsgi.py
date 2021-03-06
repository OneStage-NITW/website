"""
WSGI config for onestage_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os
import sys

# assuming your django settings file is at '/home/onestagenitwweb/mysite/settings.py'
path = '/home/onestagenitwweb/website'
if path not in sys.path:
   sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'onestage_website.settings'

# then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()