from django.db import models
from clusters.models import Host

# Create your models here.

class Rule(models.Model):

  CONNECTION_TYPE = (
      ('TCP','TCP'),
      ('UDP','UDP'),
      ('ICMP','ICMP'),
      )

  source = models.ForeignKey(Host, related_name='rule_source')
  destination = models.ForeignKey(Host, related_name='rule_destination')

  source_ip = models.IPAddressField()
  destination_ip = models.IPAddressField()

  port_number = models.IntegerField(default=0)
  connection_type = models.CharField(max_length=4, choices=CONNECTION_TYPE, default='TCP')
  approved = models.BooleanField(default=False)
  status = models.BooleanField(default=False)

  last_updated = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = (('source','destination','port_number','connection_type'),)

  def __str__(self):
    return "Rule ID " + str(self.id)
