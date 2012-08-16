import os.path

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.core.urlresolvers import get_script_prefix
from django.contrib.auth.views import redirect_to_login

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

        if request.path == "%sxmlrpc/" % get_script_prefix():
            return None

        if settings.DEBUG:
            prefix = os.path.commonprefix( [ request.path, settings.STATIC_URL ] )
            if prefix == settings.STATIC_URL:
                return None

        if not request.user.is_authenticated():
            return redirect_to_login(request.path)

        return HttpResponseForbidden('<h1>Access Denied</h1>')
