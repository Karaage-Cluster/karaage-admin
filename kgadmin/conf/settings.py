# Django settings for kgadmin project.

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
DATABASE_PASSWORD = ''         # Not used with sqlite3.
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

# Make this unique, and don't share it with anybody. AKA CHANGE THIS!
SECRET_KEY = '%g6mqnpu)l!$*1dlav#!$bc9bhnufvj)878uug2$6ize_9jn0c'



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

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: "/accounts/users/%s/" % o.username,
}

###
### Karaage settings
###

# Do new cluster accounts need a 2nd stage of approval
ADMIN_APPROVE_ACCOUNTS = True

PERSONAL_DATASTORE = 'karaage.datastores.ldap_datastore'

ACCOUNT_DATASTORES = {
    1: 'karaage.datastores.ldap_datastore',
}

ACCOUNTS_EMAIL_FROM = 'accounts@example.com'


###
### Placard Settings
### see - https://code.arcs.org.au/hudson/job/Placard/javadoc/
###


LDAP_URL = 'ldap://ldap.example.com'
LDAP_BASE = 'dc=example, dc=com'
LDAP_USER_BASE='ou=People, %s' % LDAP_BASE
LDAP_GROUP_BASE='ou=Groups, %s' % LDAP_BASE
LDAP_USE_TLS = False
LDAP_ADMIN_USER = 'cn=admin,dc=example,dc=org'
LDAP_ADMIN_PASSWORD = 'secret'
LDAP_LOCK_DN = 'cn=locked,dc=example,dc=org'

###
### Django PBS settings
###


LOCAL_PBS_SERVERS = [
    'cluster1.example.com',
    'cluster2.example.com',
]
