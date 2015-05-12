# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_auto_20150409_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 23, 18, 59, 841682, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 23, 19, 10, 381358, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
