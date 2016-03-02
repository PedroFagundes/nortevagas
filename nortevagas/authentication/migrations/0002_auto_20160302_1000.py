# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(default=b'EMPLOYEE', max_length=40, choices=[(b'EMPLOYEE', b'Candidato'), (b'EMPLOYER', b'Empregador')]),
        ),
    ]
