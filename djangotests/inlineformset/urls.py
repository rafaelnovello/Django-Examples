from django.conf.urls import patterns, url

urlpatterns = patterns('inlineformset',
    url(r'^author/(?P<author_id>\d+)/books/add/$', 'views.add_books'),
    url(r'^author/add/$', 'views.manage_authors'),
    url(r'^author/books/add/$', 'views.add_author_and_books'),
)
