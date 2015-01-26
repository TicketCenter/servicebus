from django.conf.urls import patterns, include, url

__author__ = 'Nils'

urlpatterns = patterns('',
	url(r'^concerts/', include('api.router.routes.concerts'))
)
