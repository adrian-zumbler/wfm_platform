from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'autentication/$',views.autentication, name='autentication'),
	)
