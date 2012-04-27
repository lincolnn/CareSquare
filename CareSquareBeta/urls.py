from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'CareSquareBeta.blog.views.home', name='home'),
    # url(r'^CareSquareBeta/', include('CareSquareBeta.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', direct_to_template,
            { 'template': 'index.html' }, 'index'),
)
