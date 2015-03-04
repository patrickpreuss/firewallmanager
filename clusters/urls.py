from django.conf.urls import patterns, url

from clusters import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)
