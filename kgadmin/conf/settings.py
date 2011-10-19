# Packaged defined Karaage-admin settings
from karaage.conf.settings import *

TEMPLATE_DIRS += (
    "/usr/share/kgadmin/templates",
)

SITE_ID = 1

ROOT_URLCONF = 'kgadmin.conf.urls'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/kgadmin_media/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/usr/share/kgadmin/media'

LOGIN_URL="/kgadmin/accounts/login/"
LOGIN_REDIRECT_URL="/kgadmin/"

TEMPLATE_CONTEXT_PROCESSORS += ('karaage.context_processors.admin',)

MIDDLEWARE_CLASSES += ('kgadmin.middleware.StaffOnly',)

USAGE_IS_PUBLIC = True

execfile("/etc/karaage/admin_settings.py")
