from django.contrib import admin

from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.db import IntegrityError
from django import forms

# Register your models here.
from firewalls.models import Rule
from clusters.models import Host


class RuleAdminForm(forms.ModelForm):
  class Meta:
    error_messages = {
        NON_FIELD_ERRORS: {
          'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
          }
        }
    
class RuleAdmin(admin.ModelAdmin):
  form = RuleAdminForm
  exclude = ('source_ip','destination_ip',)

  list_display = ('source','destination','source_ip','destination_ip','port_number', 'connection_type','approved','status','last_updated')
  list_filter = ['status']

  def save_model(self,request,obj,form,change):

    src_ip = Host.objects.filter(host_name=obj.source)[0].ip_address
    dest_ip	= Host.objects.filter(host_name=obj.destination)[0].ip_address
    obj.source_ip =	src_ip
    obj.destination_ip = dest_ip
    obj.save()


admin.site.register(Rule,RuleAdmin)
