from django.contrib import admin

# Register your models here.

from clusters.models import Cluster,Host,Location

class ClusterAdmin(admin.ModelAdmin):
	list_display = ('cluster_name','location')

class HostAdmin(admin.ModelAdmin):
	list_display = ('host_name','ip_address','cluster')

admin.site.register(Cluster,ClusterAdmin)
admin.site.register(Host,HostAdmin)
admin.site.register(Location)
