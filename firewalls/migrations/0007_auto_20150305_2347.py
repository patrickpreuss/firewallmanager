# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firewalls', '0006_auto_20150305_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='connection_type',
            field=models.CharField(default=b'TCP', max_length=4, choices=[(b'TCP', b'TCP'), (b'UDP', b'UDP'), (b'ICMP', b'ICMP')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rule',
            name='port_number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
