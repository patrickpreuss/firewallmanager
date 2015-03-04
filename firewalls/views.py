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
	context_dict['badcount'] = len(Rule.objects.filter(status=False))
	context_dict['goodcount'] = len(Rule.objects.filter(status=True))
	context_dict['tcpcount'] = len(Rule.objects.filter(connection_type="TCP"))
	context_dict['udpcount'] = len(Rule.objects.filter(connection_type="UDP"))
	context_dict['icmpcount'] = len(Rule.objects.filter(connection_type="ICMP"))
	context_dict['rulecount'] = len(Rule.objects.all())
	context_dict['clustercount'] = len(Cluster.objects.all())
	context_dict['locationcount'] = len(Location.objects.all())
	context_dict['hostcount'] = len(Host.objects.all())

	context_dict['hosts'] = Host.objects.all()

	return render(request, 'firewalls/index.html', context_dict)
