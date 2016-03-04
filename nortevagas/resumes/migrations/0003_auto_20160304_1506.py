# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0002_auto_20160304_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.ForeignKey(related_name='resume_of_education', blank=True, to='resumes.Education', null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.ForeignKey(related_name='resume_of_experience', blank=True, to='resumes.Experience', null=True),
        ),
    ]
