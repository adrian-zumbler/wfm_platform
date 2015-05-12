# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0004_auto_20150415_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='end_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
