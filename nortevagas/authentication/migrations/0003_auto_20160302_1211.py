# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20160302_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(default=b'EMPLOYEE', max_length=40, choices=[(b'EMPLOYEE', b'... me candidatar'), (b'EMPLOYER', b'... contratar')]),
        ),
    ]
