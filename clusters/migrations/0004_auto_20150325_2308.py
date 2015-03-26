# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0003_auto_20150325_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 23, 7, 55, 915053, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cluster',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 23, 8, 0, 147026, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 23, 8, 3, 963023, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 23, 8, 10, 458720, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
