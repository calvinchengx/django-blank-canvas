from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
    url(r'^$', 'homepage.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# In order for Dev Server to serve media files for the frontend site.
urlpatterns += staticfiles_urlpatterns()

try:
    if settings.DEBUG: # defined in manage.py when the first arg is "runserver"
        import os
        urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
                            (r'^media-admin/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.ADMIN_MEDIA_ROOT}),
                           )
except NameError:
    pass

