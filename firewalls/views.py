from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView, DetailView, TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from firewalls.serializers import FirewallSerializer
from firewalls.models import Rule
from clusters.models import Host,Cluster,Location
from rest_framework import viewsets,permissions

#from django.views.decorators.csrf import csrf_exempt

import socket



#@csrf_exempt
class RuleViewSet(viewsets.ModelViewSet):
	queryset = Rule.objects.all()
	serializer_class = FirewallSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@login_required(login_url="/login")
def IndexView(request):
	context_dict = {}

	context_dict['rule_list'] = Rule.objects.all().order_by('-last_updated')
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


class HostListView(ListView):
	model = Host
	template_name='firewalls/host_list.html'

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(HostListView, self).dispatch(*args, **kwargs)


class LocationListView(ListView):
	model=Location
	template_name='firewalls/location_list.html'

	@method_decorator(login_required(login_url="/login"))
	def dispatch(self, *args, **kwargs):
		return super(LocationListView, self).dispatch(*args, **kwargs)

@login_required(login_url="/login")
@csrf_exempt
def FirewallTest(request):
	# return HttpResponse("Starting Ajax")
	print request.method
	print request.user

	if request.is_ajax():
		print "request is ajax"
		if request.method=='POST':
			print request.POST.get('name')
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((request.POST.get('name'),22))
				print result

				if result == 0:
					return JsonResponse({"msg": "True"})
				else:
					return JsonResponse({"msg" : "False"})


			except:
				return JsonResponse({"msg" : "con failed"})

			# if result == 0:
   # 				print "Port is open"
			# 	return JsonResponse({"msg":"connection succesfull"})
			# else:
   # 				print "Port is not open"
			# 	return JsonResponse({"msg":"connection failed"})

	else:
		print "request is not ajax"


	# if request.method == 'GET':
	# 	# return JsonResponse({'msg' : 'starting ajax'})
	# 	return JsonResponse({"msg" : "hi"})
	# elif request.method =='POST':
	# 	print "Request is POST"
	# 	print request.POST.get('name')
	# 	return JsonResponse({'msg' : 'json'})
