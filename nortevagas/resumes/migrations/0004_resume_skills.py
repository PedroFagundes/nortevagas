# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0003_auto_20160304_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Compet\xc3\xaancias', blank=True),
        ),
    ]
