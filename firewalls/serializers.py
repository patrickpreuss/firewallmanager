from rest_framework import serializers
from firewalls.models import Rule

class FirewallSerializer(serializers.ModelSerializer):

	source = serializers.StringRelatedField()
	destination = serializers.StringRelatedField()

	class Meta:
		model = Rule
		fields = ('id','source','destination','source_ip','destination_ip','port_number','connection_type','approved','status')
		read_only_fields = ('source_ip','destination_ip','port_number','connection_type','approved',)
