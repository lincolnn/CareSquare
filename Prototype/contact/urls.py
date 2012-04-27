from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('contact.views',
    url(r'^contact/$', contact_form, name="contact_form"),
    url(r'^contact/success/$', direct_to_template, {'template': 'contact/success.html'},
        name="contact_success"),
)
