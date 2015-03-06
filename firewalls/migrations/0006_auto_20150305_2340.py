# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firewalls', '0005_auto_20150305_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='connection_type',
            field=models.CharField(max_length=4, choices=[(b'TCP', b'TCP'), (b'UDP', b'UDP'), (b'ICMP', b'ICMP')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rule',
            name='port_number',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
