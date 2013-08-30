# Packaged defined Karaage-admin settings
from karaage.conf.settings import *

AJAX_LOOKUP_CHANNELS = {
    'person' : ( 'karaage.people.lookups', 'PersonLookup'),
    'group' : ( 'karaage.people.lookups', 'GroupLookup'),
    'project' : ( 'karaage.projects.lookups', 'ProjectLookup'),
}

TEMPLATE_DIRS += (
    "/usr/share/kgadmin/templates",
)

SITE_ID = 1

ROOT_URLCONF = 'kgadmin.conf.urls'

STATIC_ROOT = '/var/lib/karaage-admin/static'
STATIC_URL = '/kgadmin_media/'

LOGIN_URL="/kgadmin/accounts/login/"
LOGIN_REDIRECT_URL="/kgadmin/"

TEMPLATE_CONTEXT_PROCESSORS += ('karaage.context_processors.admin',)

MIDDLEWARE_CLASSES += ('kgadmin.middleware.StaffOnly',)

USAGE_IS_PUBLIC = True

execfile("/etc/karaage/admin_settings.py")
