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

    url(r'^host/list/$', views.HostListView.as_view(), name='host-details'),
    url(r'^location/list/$', views.LocationListView.as_view(), name='location-details'),
    url(r'^location/create/$', views.LocationCreateView.as_view(), name='location-create'),
    url(r'^location/update/(?P<pk>\d+)/$', views.LocationUpdateView.as_view(), name='location-update'),
    url(r'^location/delete/(?P<pk>\d+)/$', views.LocationDelete.as_view(), name='location-delete'),

    url(r'^firewalltest/', views.FirewallTest, name='firewall-test' ),


    url(r'^cluster/list/$', views.ClusterListView.as_view(), name='cluster-details'),
    url(r'^cluster/create/$', views.ClusterCreate.as_view(), name='cluster-create'),
    url(r'^cluster/update/(?P<pk>\d+)/$', views.ClusterUpdate.as_view(), name='cluster-update'),
    url(r'^cluster/delete/(?P<pk>\d+)/$', views.ClusterDelete.as_view(), name='cluster-delete'),





    #url(r'^clusters/', include('clusters.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
admin.site.site_header = "Firewall Rules Validator"
admin.site.index_title = "Firewall Rules Validator"
admin.site.site_title = "Firewall Rules Validator"
