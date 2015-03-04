from django.db import models

# Create your models here.
class Location(models.Model):
	location_name = models.CharField(max_length=50)

	def __str__(self):
		return self.location_name

class Cluster(models.Model):
	cluster_name = models.CharField(max_length=50)
	location = models.ForeignKey(Location)

	def __str__(self):
		return self.cluster_name

class Host(models.Model):
	host_name = models.CharField(max_length=50,unique=True)
	ip_address = models.IPAddressField(unique=True)
	cluster = models.ForeignKey(Cluster)
    
 	class Meta:
		unique_together = ("host_name","ip_address")

	def __str__(self):
		return self.host_name
