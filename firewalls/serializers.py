from rest_framework import serializers
from firewalls.models import Rule

from rest_framework.validators import UniqueTogetherValidator

class FirewallSerializer(serializers.ModelSerializer):

  source = serializers.StringRelatedField()
  destination = serializers.StringRelatedField()
  #port_number = serializers.IntegerField(default=serializers.CreateOnlyDefault(0))
  port_number = serializers.ReadOnlyField()
  connection_type = serializers.ReadOnlyField()
  #connection_type = serializers.CharField(default=serializers.CreateOnlyDefault('TCP'))

  class Meta:
    model = Rule
    fields = ('id','source','destination','source_ip','destination_ip','port_number','connection_type','approved','status')
    read_only_fields = ('source_ip','destination_ip','port_number','connection_type','approved',)

#    validators = [
#        UniqueTogetherValidator(
#          queryset=Rule.objects.all(),
#          fields=('source','destination','port_number','connection_type')
#          )
#        ]
