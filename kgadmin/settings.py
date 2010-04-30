
AUTH_PROFILE_MODULE = 'people.Person'

GRAPH_DEBUG = False
GRAPH_LIB = 'karaage.graphs.matplotlib9'
GRAPH_ROOT = '/var/cache/kgadmin/graphs'
GRAPH_URL = '/kgadmin_graphs/'

DEFAULT_MC = 1

SHELLS = ( ('/bin/bash','bash'),
           ('/bin/csh', 'csh'),
           ('/bin/ksh', 'ksh'),
           ('/bin/tcsh', 'tcsh'),
           ('/bin/zsh', 'zsh'), )
   

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'andsome.layout',
    'andsome',
    'django_surveys',
    'karaage',
    'karaage.people',
    'karaage.machines',
    'karaage.institutes',
    'karaage.projects',
    'karaage.usage',
    'karaage.requests',
    'karaage.cache',
    'karaage.software',
    'karaage.pbsmoab',
    'karaage.projectreports',
    'karaage.emails',
    'placard.lgroups',
    'placard.lusers',
    'django_xmlrpc',
    'django_pbs.servers',
    'django_pbs.jobs',
    'django.contrib.comments',

)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/etc/kgadmin/templates-local",
    "/usr/share/kgadmin/templates",
)

ROOT_URLCONF = 'kgadmin.conf.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'karaage.context_processors.common',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/kgadmin_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/django_media/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/usr/share/kgadmin/media'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

AUTHENTICATION_BACKENDS = (
    'placard.backends.LDAPBackend',
)

LDAP_ATTRS = 'kgadmin.conf.ldap_attrs'
LDAP_PASSWD_SCHEME = 'md5-crypt'

from os import uname
SERVER_EMAIL = 'karaage@' + uname()[1]
EMAIL_HOST = 'localhost'
EMAIL_SUBJECT_PREFIX = '[Karaage] - '

SEND_BROKEN_LINK_EMAILS = True

from conf.settings import *
