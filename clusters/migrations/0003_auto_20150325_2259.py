# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0002_auto_20150302_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 22, 59, 14, 680694, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 22, 59, 22, 487960, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
