# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firewalls', '0002_auto_20150219_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 1, 1, 17, 131484, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
