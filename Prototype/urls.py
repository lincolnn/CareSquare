from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Prototype.blog.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.urls')), # registration 4/21 
    url(r'^polls/', include('polls.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$/', 'main'), # forums urlconf coincides with blog temp
    url(r'^forum/(\d+)/$', 'forum'),
    url(r'^thread/(\d+)/$', 'thread'),
    #patterns for contact forms
    url(r'^contact/$', include('contact.urls')),
)
