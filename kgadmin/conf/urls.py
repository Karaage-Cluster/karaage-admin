from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib.admin.models import LogEntry

import ajax_select.urls
import placard.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'karaage.views.admin_index', name='kg_admin_index'),

    url(r'^lookup/', include(ajax_select.urls)),

    url(r'^search/$', 'karaage.views.search', name='kg_site_search'), 

    url(r'^password/$', placard.views.UserChangePassword.as_view(), name='plac_user_password'),
    url(r'^users/(?P<username>[-.\w]+)/ldap/$', placard.views.AccountVerbose.as_view()),

    url(r'^users/', include('karaage.people.urls.admin')),
    url(r'^institutes/', include('karaage.institutes.urls.admin')),
    url(r'^projects/', include('karaage.projects.urls.admin')),
    url(r'^machines/', include('karaage.machines.urls')),
    url(r'^usage/', include('karaage.usage.urls.admin')),
    url(r'^software/', include('karaage.software.urls.admin')),
    url(r'^projectreports/', include('karaage.projectreports.urls.admin')),
    url(r'^surveys/', include('django_surveys.urls')),
    url(r'^pbsmoab/', include('karaage.pbsmoab.urls')),
    url(r'^emails/', include('karaage.emails.urls')),
    url(r'^applications/', include('karaage.applications.urls.admin')),

    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^pbs/', include('django_pbs.servers.urls')),                  
    url(r'^lusers/', include('placard.user_urls')),                  
    url(r'^lgroups/', include('placard.group_urls')),
    url(r'^misc/$', 'django.views.generic.simple.direct_to_template', {'template': 'misc/index.html'}, name='kg_misc'),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc',),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),                   

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),

)

log_dict = {
    'queryset': LogEntry.objects.select_related(),
    'paginate_by': 50,
    'template_name': 'log_list.html',
    'template_object_name': 'log',
}

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^logs/$', 'object_list', log_dict, name='kg_log_list'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^kgadmin_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^karaage_graphs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GRAPH_ROOT}),
    )		

execfile("/etc/karaage/admin_urls.py")
