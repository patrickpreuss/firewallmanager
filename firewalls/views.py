from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

# Create your views here.
from firewalls.serializers import FirewallSerializer
from firewalls.models import Rule
from clusters.models import Host,Cluster,Location
from rest_framework import viewsets,permissions

#from django.views.decorators.csrf import csrf_exempt


#@csrf_exempt

class RuleViewSet(viewsets.ModelViewSet):
	queryset = Rule.objects.all()
	serializer_class = FirewallSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



#class IndexView(generic.ListView):
#	template_name = 'firewalls/index.html'
#	context_object_name = 'rule_list'


#	def get_queryset(self):
#		return Rule.objects.all()

#	def get_count():
#		badcount = Rule.objects.filter(status='False')
#		return badcount
	
#	rule_list['badcount'] = get_count()

#class DetailView(generic.DetailView):
#	model = Rule
#	template_name = 'firewalls/detail.html'

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
