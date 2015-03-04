# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('port_number', models.IntegerField(default=0)),
                ('connection_type', models.CharField(default=b'TCP', max_length=4, choices=[(b'TCP', b'TCP'), (b'UDP', b'UDP'), (b'ICMP', b'ICMP')])),
                ('approved', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('destination', models.ForeignKey(related_name='rule_destination', to='clusters.Host')),
                ('destination_ip', models.ForeignKey(related_name='rule_destinationip', to='clusters.Host', to_field=b'ip_address')),
                ('source', models.ForeignKey(related_name='rule_source', to='clusters.Host')),
                ('source_ip', models.ForeignKey(related_name='rule_sourceip', to='clusters.Host', to_field=b'ip_address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
