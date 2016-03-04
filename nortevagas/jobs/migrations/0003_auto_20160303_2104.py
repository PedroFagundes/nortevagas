# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobbookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='application_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 0, 4, 57, 349142, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='candidate_cover_letter',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='employer_note',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='rating',
            field=models.SmallIntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(default=b'NEW', max_length=25, choices=[(b'NEW', b'Nova'), (b'INTERVIEWED', b'Entrevistado'), (b'HIRED', b'Contratado'), (b'ARCHIVED', b'Arquivado')]),
        ),
    ]
