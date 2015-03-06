# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firewalls', '0004_auto_20150304_0027'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rule',
            unique_together=set([('source', 'destination', 'port_number', 'connection_type')]),
        ),
    ]
