from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from api.Artists import Artists

urlpatterns = patterns('',
                       url(r'^$', cache_page(60 * 60 * 24 * 7)(Artists().get_artists)),
                       url(r'^(?P<name>[\w\W]+)/$', cache_page(60 * 60 * 24 * 7)(Artists().get_artist))
)
