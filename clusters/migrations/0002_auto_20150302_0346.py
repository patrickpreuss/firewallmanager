# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='host',
            unique_together=set([('host_name', 'ip_address')]),
        ),
    ]
