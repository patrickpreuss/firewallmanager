from django.conf.urls import patterns, url

from firewalls import views

urlpatterns = patterns('firewalls.views',
#	url(r'^$', views.IndexView.as_view()),
	url(r'^$', 'IndexView'),
#	url(r'^rules/$', 'RuleList'),
#	url(r'^rules/(?P<pk>[0-9]+)/$', 'RuleDetail'),
)
