# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20150408_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=1, choices=[(b'Baja', b'baja'), (b'Activo', b'activo')])),
                ('min_hours', models.IntegerField()),
                ('max_hours', models.IntegerField()),
                ('css_number', models.IntegerField()),
                ('avaya_number', models.IntegerField()),
                ('organization', models.ForeignKey(to='organization.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
