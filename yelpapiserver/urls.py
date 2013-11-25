from django.conf.urls import patterns, include, url
from django.contrib import admin

# This function iterates over your INSTALLED_APPS setting and looks for a file
# named admin.py in each installed app. If one exists, it executes that file
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^admin/', include(admin.site.urls)),
    url(r'^search$', 'yelpapiserver.views.search', name = 'search')
)
