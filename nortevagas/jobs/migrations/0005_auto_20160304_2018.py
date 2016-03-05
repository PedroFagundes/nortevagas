# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20160304_1144'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='jobbookmark',
            unique_together=set([('job', 'candidate')]),
        ),
    ]
