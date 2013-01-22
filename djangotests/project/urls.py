from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'home.html'}),
    url(r'^inlines/', include('inlineformset.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
