from django.conf.urls import patterns, url

from api.Orders import Orders

urlpatterns = patterns('',
    url(r'^$', Orders().post_order_unregistered_user),
    url(r'^(?P<user_id>[\d]+)/(?P<token>[\w\W]+)/$', Orders().order_registered_user),
    url(r'^(?P<user_id>[\d]+)/(?P<token>[\w\W]+)/$', Orders().get_order_registered_user)
)
