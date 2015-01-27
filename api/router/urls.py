from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^/concerts/', include('api.router.routes.concerts')),
    url(r'^/artists/', include('api.router.routes.artists')),
    url(r'^/users/', include('api.router.routes.users')),
    url(r'^/orders/', include('api.router.routes.orders'))
)
