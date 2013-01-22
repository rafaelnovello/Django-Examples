from django.conf.urls import patterns, url

urlpatterns = patterns('inlineformset',
    url(r'^$', 'views.authors_list'),
    url(r'^author/add/$', 'views.author_add'),
    url(r'^author/edit/(?P<pk>\d+)$', 'views.author_edit'),
    url(r'^author/delete/(?P<pk>\d+)$', 'views.author_delete'),
)
