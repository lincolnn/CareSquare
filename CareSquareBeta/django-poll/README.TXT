Django poll system


Requirements

Django 1.3
JQuery (There are some problems with animation in older versions.) 
Django Internationalization (optionally)


Installation

Download or clone repository into the folder you like. Unpack it if needed and make an installation. The installation is simple, just type next command:
   >> python setup.py install

Now you should config your site to use the poll application. Follow instructions below:


1. Add the name of the application at the end of your INSTALLED_APPS (in settings.py), like this:

INSTALLED_APPS = (
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'django.contrib.staticfiles',
'django.contrib.admin',
'django.contrib.admindocs',

'poll',
)


2. Add the poll's url to your urls.py.

from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import TestView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TestView.as_view(), name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^poll/', include('poll.urls')),
)

urlpatterns += staticfiles_urlpatterns()


3. Your TEMPLATE_CONTEXT_PROCESSORS (in settings.py) should looks like this:

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
) 


4. Eventually we need to do "syncdb".
   >> python manage.py syncdb

ATTENTION: Don't forget this step. It's very important, because django-poll-system have a fixture that needs to be installed to DB.

----

Now installation is completed. After all, you have some data out of the box. And it's time to show the poll on your site. Add {% load polls_tags %} at the top of your page and insert {% poll_queue 'Public' %} to the place you want to see the django-poll-system component. Of course the script of JQuery library must be included (<script type="text/javascript" src="your/path/to/jquery.js"></script>) before you call "poll_queue".

That's all. Try an example: http://polltest.pythonism.ru. (Please, leave your comments there)
