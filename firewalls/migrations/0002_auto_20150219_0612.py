# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firewalls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='destination_ip',
            field=models.IPAddressField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rule',
            name='source_ip',
            field=models.IPAddressField(),
            preserve_default=True,
        ),
    ]
