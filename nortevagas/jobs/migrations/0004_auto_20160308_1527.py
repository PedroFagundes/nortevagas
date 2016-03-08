# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_benefits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='requirements',
            field=models.CharField(max_length=250, null=True, verbose_name='Requisitos do candidato', blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='responsabilities',
            field=models.CharField(max_length=250, null=True, verbose_name='Responsabilidades', blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(unique=True, max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100, verbose_name='T\xedtulo'),
        ),
    ]
