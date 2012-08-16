# Packaged defined Karaage-admin settings
from karaage.conf.settings import *

TEMPLATE_DIRS += (
    "/usr/share/kgadmin/templates",
)

SITE_ID = 1

ROOT_URLCONF = 'kgadmin.conf.urls'

STATIC_ROOT = '/var/lib/karaage-admin/static'
STATIC_URL = '/kgadmin_media/'
ADMIN_MEDIA_PREFIX = '/kgadmin_media/admin/'

LOGIN_URL="/kgadmin/accounts/login/"
LOGIN_REDIRECT_URL="/kgadmin/"

TEMPLATE_CONTEXT_PROCESSORS += ('karaage.context_processors.admin',)

MIDDLEWARE_CLASSES += ('kgadmin.middleware.StaffOnly',)

USAGE_IS_PUBLIC = True

AJAX_SELECT_BOOTSTRAP = False
AJAX_SELECT_INLINES = None

execfile("/etc/karaage/admin_settings.py")
