from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from firewalls import views

router = routers.DefaultRouter()
router.register(r'^', views.RuleViewSet)

urlpatterns = patterns('',
       # Examples:
       # url(r'^$', 'fwmanager.views.home', name='home'),
       # url(r'^blog/', include('blog.urls')),
       #url(r'^', include(router.urls)),


    url(r'^$', include('firewalls.urls')),
    url(r'^api', include(router.urls)),
    url(r'^logout/', 'django.contrib.auth.views.logout',{'next_page':'/'}),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'firewalls/login.html'}),
    url(r'^about', views.AboutView.as_view(), name='about-view'),


    # Host CRUD URL Conf
    url(r'^host/list/$', views.HostListView.as_view(), name='host-details'),
    url(r'^host/create/$', views.HostCreate.as_view(), name='host-create'),
    url(r'^host/update/(?P<pk>\d+)/$', views.HostUpdate.as_view(), name='host-update'),
    url(r'^host/delete/(?P<pk>\d+)/$', views.HostDelete.as_view(), name='host-delete'),


    # Location CRUD URL Conf
    url(r'^location/list/$', views.LocationListView.as_view(), name='location-details'),
    url(r'^location/create/$', views.LocationCreateView.as_view(), name='location-create'),
    url(r'^location/update/(?P<pk>\d+)/$', views.LocationUpdateView.as_view(), name='location-update'),
    url(r'^location/delete/(?P<pk>\d+)/$', views.LocationDelete.as_view(), name='location-delete'),


    # Cluster CRUD URL Conf
    url(r'^cluster/list/$', views.ClusterListView.as_view(), name='cluster-details'),
    url(r'^cluster/create/$', views.ClusterCreate.as_view(), name='cluster-create'),
    url(r'^cluster/update/(?P<pk>\d+)/$', views.ClusterUpdate.as_view(), name='cluster-update'),
    url(r'^cluster/delete/(?P<pk>\d+)/$', views.ClusterDelete.as_view(), name='cluster-delete'),

    # Rule CRUD URL Conf

    url(r'^rule/list/$', views.RuleList.as_view(), name='rule-details'),
    url(r'^rule/create/$', views.RuleCreate.as_view(), name='rule-create'),
    url(r'^rule/update/(?P<pk>\d+)/$', views.RuleUpdate.as_view(), name='rule-update'),
    url(r'^rule/delete/(?P<pk>\d+)/$', views.RuleDelete.as_view(), name='rule-delete'),
    # End of Rule CRUD URL Conf

    url(r'^firewalltest/', views.FirewallTest, name='firewall-test' ),


    #url(r'^clusters/', include('clusters.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
admin.site.site_header = "Firewall Rules Validator"
admin.site.index_title = "Firewall Rules Validator"
admin.site.site_title = "Firewall Rules Validator"
