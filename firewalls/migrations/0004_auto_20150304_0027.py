# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firewalls', '0003_rule_last_updated'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rule',
            unique_together=set([('source_ip', 'destination_ip', 'port_number', 'connection_type')]),
        ),
    ]
