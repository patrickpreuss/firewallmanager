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

	url(r'^api', include(router.urls)),

	url(r'^$', include('firewalls.urls')),
    #url(r'^clusters/', include('clusters.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
admin.site.site_header = "Firewall Manager"
admin.site.index_title = "Firewall Manager"
admin.site.site_title = "Firewall Manager"
