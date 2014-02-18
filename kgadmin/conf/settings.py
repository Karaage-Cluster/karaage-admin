# Packaged defined Karaage-admin settings
from karaage.conf.settings import *

SITE_ID = 1

ROOT_URLCONF = 'kgadmin.conf.urls'

STATIC_ROOT = '/var/lib/karaage-admin/static'
STATIC_URL = '/kgadmin_media/'

ADMIN_REQUIRED = True

execfile("/etc/karaage/admin_settings.py")
