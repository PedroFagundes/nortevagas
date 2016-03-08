# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20160308_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='benefits',
            field=models.CharField(max_length=150, null=True, verbose_name='Benef\xedcios', blank=True),
        ),
    ]
