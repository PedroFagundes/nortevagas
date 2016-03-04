# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20160303_2104'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='jobapplication',
            unique_together=set([('job', 'candidate')]),
        ),
    ]
