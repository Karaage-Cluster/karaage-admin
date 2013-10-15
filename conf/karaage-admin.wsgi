import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'kgadmin.conf.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
