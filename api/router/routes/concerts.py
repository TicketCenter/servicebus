from django.conf.urls import patterns, url

from api.Concerts import Concerts


__author__ = 'Nils'

urlpatterns = patterns('',
    url(r'^$', Concerts().concerts),
    url(r'^(?P<concert_id>.{1,50})/$', Concerts().concert)
)
