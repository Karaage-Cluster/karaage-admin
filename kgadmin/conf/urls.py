from django.conf.urls import *
from django.conf import settings

import ajax_select.urls

urlpatterns = patterns('',
    url(r'^$', 'karaage.admin.views.admin_index', name='index'),
    url(r'^search/$', 'karaage.admin.views.search', name='kg_site_search'),
    url(r'^misc/$', 'karaage.admin.views.misc', name='kg_misc'),

    url(r'^lookup/', include(ajax_select.urls)),

    url(r'^persons/', include('karaage.people.urls.persons')),
    url(r'^profile/', include('karaage.people.urls.profile')),
    url(r'^groups/', include('karaage.people.urls.groups')),
    url(r'^institutes/', include('karaage.institutes.urls')),
    url(r'^projects/', include('karaage.projects.urls')),
    url(r'^machines/', include('karaage.machines.urls')),
    url(r'^usage/', include('karaage.usage.urls')),
    url(r'^software/', include('karaage.software.urls')),
    url(r'^emails/', include('karaage.emails.urls')),
    url(r'^applications/', include('karaage.applications.urls')),

    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc',),

    url(r'^logs/$', 'karaage.admin.views.log_list', name='kg_log_list'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^karaage_graphs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GRAPH_ROOT}),
    )

execfile("/etc/karaage/admin_urls.py")
