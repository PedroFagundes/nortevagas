# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0004_resume_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, blank=True),
        ),
    ]
