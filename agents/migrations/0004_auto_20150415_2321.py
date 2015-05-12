# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_auto_20150415_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='end_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
