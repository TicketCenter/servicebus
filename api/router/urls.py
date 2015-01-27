from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^/concerts/', include('api.router.routes.concerts')),
    url(r'^/artists/', include('api.router.routes.artists'))
)
