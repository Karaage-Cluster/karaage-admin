import os.path

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

class StaffOnly(object):
    def process_request(self, request):
        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "The Karaage StaffOnly middleware requires the"
                " authentication middleware to be installed.  Edit your"
                " MIDDLEWARE_CLASSES setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the StaffOnly class.")

        if request.user.is_staff:
            return None

        if request.path == settings.LOGIN_URL:
            return None

        if request.path == settings.LOGOUT_URL:
            return None

        if request.path == "/accounts/xmlrpc/":
            return None

        if settings.DEBUG:
            prefix = os.path.commonprefix( [ request.path, settings.MEDIA_URL ] )
            if prefix == settings.MEDIA_URL:
                return None

        if not request.user.is_authenticated():
            return HttpResponseRedirect(settings.LOGIN_URL)

        return HttpResponseForbidden('<h1>Access Denied</h1>')
