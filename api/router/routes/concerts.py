from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from api.Concerts import Concerts

urlpatterns = patterns('',
                       url(r'^$', cache_page(60 * 60 * 24 * 7)(Concerts().get_concerts)),
                       url(r'^(?P<id>.{1,50})/$', cache_page(60 * 60 * 24 * 7)(Concerts().get_concert))
)
