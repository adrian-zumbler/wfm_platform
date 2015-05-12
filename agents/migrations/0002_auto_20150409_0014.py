# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'Baja', b'baja'), (b'Activo', b'activo')]),
            preserve_default=True,
        ),
    ]
