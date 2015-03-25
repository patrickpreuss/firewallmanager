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

       url(r'^clusters/$', views.ClusterListView.as_view(), name='cluster-details'),
       url(r'^hosts/$', views.HostListView.as_view(), name='host-details'),
       url(r'^locations/$', views.LocationListView.as_view(), name='location-details'),

       url(r'^firewalltest/', views.FirewallTest, name='firewall-test' ),


    #url(r'^clusters/', include('clusters.urls')),
       url(r'^admin/', include(admin.site.urls)),
                       )
admin.site.site_header = "Firewall Rules Validator"
admin.site.index_title = "Firewall Rules Validator"
admin.site.site_title = "Firewall Rules Validator"
