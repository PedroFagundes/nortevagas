# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobBookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidate', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(to='jobs.Job')),
            ],
            options={
                'verbose_name': 'Vaga favorita de Usuario',
                'verbose_name_plural': 'Vagas favoritas de Usuarios',
            },
        ),
    ]
