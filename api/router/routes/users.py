from django.conf.urls import patterns, url

from api.Users import Users

urlpatterns = patterns('',
    url(r'^$', Users().post_user),
    url(r'^login/$', Users().post_user_login),
    url(r'^(?P<id>[\d]+)/(?P<token>[\w\W]+)/$', Users().user_info)
)
