from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView, DetailView, TemplateView, CreateView,UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from firewalls.serializers import FirewallSerializer
from firewalls.models import Rule
from clusters.models import Host,Cluster,Location
from rest_framework import viewsets,permissions

#from django.views.decorators.csrf import csrf_exempt

import zerorpc




#@csrf_exempt
class RuleViewSet(viewsets.ModelViewSet):
	queryset = Rule.objects.all()
	serializer_class = FirewallSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@login_required(login_url="/login")
def IndexView(request):
	context_dict = {}

        context_dict['rule_list'] = Rule.objects.all().order_by('-last_updated')[:5]
	context_dict['badcount'] = Rule.objects.filter(status=False).count()
	context_dict['goodcount'] = Rule.objects.filter(status=True).count()
	context_dict['tcpcount'] = Rule.objects.filter(connection_type="TCP").count()
	context_dict['udpcount'] = Rule.objects.filter(connection_type="UDP").count()
	context_dict['icmpcount'] = Rule.objects.filter(connection_type="ICMP").count()
	context_dict['rulecount'] = Rule.objects.all().count()
	context_dict['clustercount'] = Cluster.objects.all().count()
	context_dict['locationcount'] = Location.objects.all().count()
	context_dict['hostcount'] = Host.objects.all().count()

        context_dict['hosts'] = Host.objects.all()

	return render(request, 'firewalls/index.html', context_dict)

class AboutView(TemplateView):
	template_name = 'firewalls/about.html'

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(AboutView, self).dispatch(*args, **kwargs)


class ClusterListView(ListView):
	model = Cluster
	template_name='firewalls/cluster_list.html'
	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(ClusterListView, self).dispatch(*args, **kwargs)

### Host CRUD Section Start ###
class HostListView(ListView):
	model = Host
	template_name='firewalls/host_list.html'

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(HostListView, self).dispatch(*args, **kwargs)

class HostCreate(CreateView):
	model=Host
	template_name='firewalls/host_create.html'
	success_url = '/host/list'
	fields = ['host_name','ip_address','cluster']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(HostCreate, self).dispatch(*args, **kwargs)

class HostUpdate(UpdateView):
	model=Host
	template_name='firewalls/host_update.html'
	success_url = '/host/list'
	fields = ['host_name','ip_address','cluster']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(HostUpdate, self).dispatch(*args, **kwargs)

class HostDelete(DeleteView):
	model=Host
	template_name='firewalls/host_confirm_delete.html'
	success_url='/host/list'
	fields = ['host_name','ip_address','cluster']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(HostDelete, self).dispatch(*args, **kwargs)

### Host CRUD Section End ###

class LocationListView(ListView):
	model=Location
	template_name='firewalls/location_list.html'

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(LocationListView, self).dispatch(*args, **kwargs)

class LocationCreateView(CreateView):
	model=Location
	template_name='firewalls/location_create.html'
	success_url = '/location/list'
	fields = ['location_name']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(LocationCreateView, self).dispatch(*args, **kwargs)

class LocationUpdateView(UpdateView):
	model=Location
	template_name='firewalls/location_update.html'
	success_url = '/location/list'
	fields = ['location_name']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(LocationUpdateView, self).dispatch(*args, **kwargs)

class LocationDelete(DeleteView):
	model=Location
	template_name='firewalls/location_confirm_delete.html'
	success_url='/location/list'
	fields = ['location_name']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(LocationDelete, self).dispatch(*args, **kwargs)

####################################
# Cluster CRUD Section
####################################
class ClusterCreate(CreateView):
	model=Cluster
	template_name='firewalls/cluster_create.html'
	success_url = '/cluster/list'
	fields = ['cluster_name','location']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(ClusterCreate, self).dispatch(*args, **kwargs)

class ClusterUpdate(UpdateView):
	model=Cluster
	template_name='firewalls/cluster_update.html'
	success_url = '/cluster/list'
	fields = ['cluster_name','location']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(ClusterUpdate, self).dispatch(*args, **kwargs)

class ClusterDelete(DeleteView):
	model=Cluster
	template_name='firewalls/cluster_confirm_delete.html'
	success_url='/cluster/list'
	fields = ['cluster_name','location']

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(ClusterDelete, self).dispatch(*args, **kwargs)


# End of Cluster CRUD Section

@login_required(login_url="/login")
@csrf_exempt
def FirewallTest(request):
	# return HttpResponse("Starting Ajax")
	print request.method
	print request.user
	print request.POST.get("name")
	if request.is_ajax():
		if request.method=='POST':
			try:
				rpcClient = zerorpc.Client()
				rpcClient.connect("tcp://127.0.0.1:4242")
				result=rpcClient.hello("RPC")
				if result == 0:
					return JsonResponse({"msg": "True"})
				else:
					return JsonResponse({"msg" : "False"})
			except:
				return JsonResponse({"msg" : "con failed"})
	else:
		return HttpResponse("Direct Access Forbidden")
