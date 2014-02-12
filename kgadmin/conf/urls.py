from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('',
)

import karaage.conf.urls
urlpatterns += karaage.conf.urls.urlpatterns


execfile("/etc/karaage/admin_urls.py")
