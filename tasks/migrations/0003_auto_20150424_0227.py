# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20150408_2351'),
        ('tags', '0001_initial'),
        ('agents', '0005_auto_20150424_0227'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_delete_taks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document', models.FileField(upload_to=b'files')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_published', models.DateField()),
                ('status', models.CharField(max_length=255, choices=[(b'Rechazada', b'Rechazada'), (b'Pendiente', b'Pendiente'), (b'Aplicada', b'Aplicada')])),
                ('agent', models.ForeignKey(to='agents.Agent')),
                ('orgzanization', models.ForeignKey(to='organization.Organization')),
                ('tag', models.ManyToManyField(to='tags.Tag')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='file',
            name='task',
            field=models.ForeignKey(to='tasks.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='tasks.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
