# Django settings for kgadmin project.
from os import uname, path as os_path
from private_settings import *

PROJECT_DIR = os_path.abspath(os_path.split(__file__)[0])

###
### Standard Django settings 
### see http://docs.djangoproject.com/en/1.1/ref/settings/#ref-settings
###

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Store in private settings
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Melbourne'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-au'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/usr/share/kgadmin/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/karaage_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/django_media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'andsome.middleware.threadlocals.ThreadLocals',
)

# Enable REMOTE_USER auth
#MIDDLEWARE_CLASSES += (
#    ('karaage.middleware.auth.ApacheSiteLogin',)
#)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'karaage.context_processors.common',
)

ROOT_URLCONF = 'kgadmin.conf.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/etc/kgadmin/templates-local",
    "/usr/share/kgadmin/templates",
)

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

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: "/accounts/users/%s/" % o.username,
}

AUTH_PROFILE_MODULE = 'people.Person'

SERVER_EMAIL = 'django@' + uname()[1]
EMAIL_HOST = 'smtp.example.com'
EMAIL_SUBJECT_PREFIX = '[Karaage] - '
SEND_BROKEN_LINK_EMAILS = True

AUTHENTICATION_BACKENDS = (
    'placard.backends.LDAPBackend',
)


###
### Karaage settings
###

GRAPH_DEBUG = True
GRAPH_LIB = 'karaage.graphs.matplotlib9'

# Do new cluster accounts need a 2nd stage of approval
ADMIN_APPROVE_ACCOUNTS = True

DEFAULT_MC = 1

PERSONAL_DATASTORE = 'karaage.datastores.ldap_datastore'

ACCOUNT_DATASTORES = {
    1: 'karaage.datastores.ldap_datastore',
}

ACCOUNTS_EMAIL_FROM = 'accounts@vpac.org'

SHELLS = ( ('/bin/bash','bash'),
           ('/bin/csh', 'csh'),
           ('/bin/ksh', 'ksh'),
           ('/bin/tcsh', 'tcsh'),
           ('/bin/zsh', 'zsh'), )
           

###
### Placard Settings
### see - https://code.arcs.org.au/hudson/job/Placard/javadoc/
###


LDAP_URL = 'ldap://ldap.example.com'
LDAP_BASE = 'dc=example, dc=com'
LDAP_USER_BASE='ou=People, %s' % LDAP_BASE
LDAP_GROUP_BASE='ou=Groups, %s' % LDAP_BASE
LDAP_ATTRS = 'kgadmin.conf.ldap_attrs'
LDAP_USE_TLS = False
LDAP_PASSWD_SCHEME = 'md5-crypt'


###
### Django PBS settings
###


LOCAL_PBS_SERVERS = [
    'cluster1.example.com',
    'cluster2.example.com',
]
