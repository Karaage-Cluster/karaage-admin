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

XMLRPC_METHODS = (
    ('karaage.pbsmoab.xmlrpc.parse_usage', 'parse_usage',),
    ('karaage.pbsmoab.xmlrpc.get_project', 'get_project',),
    ('karaage.pbsmoab.xmlrpc.project_under_quota', 'project_under_quota',),
    ('karaage.pbsmoab.xmlrpc.showquota', 'showquota',),
    ('karaage.pbsmoab.xmlrpc.get_disk_quota', 'get_disk_quota',),
    ('karaage.pbsmoab.xmlrpc.change_default_project', 'change_default_project',),
)


execfile("/etc/karaage/admin_settings.py")
