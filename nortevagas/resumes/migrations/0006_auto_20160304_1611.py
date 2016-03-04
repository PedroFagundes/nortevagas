# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0005_resume_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='content',
        ),
        migrations.AddField(
            model_name='resume',
            name='about',
            field=models.TextField(default='Sobre o camarada', max_length=500, verbose_name=b'Sobre'),
            preserve_default=False,
        ),
    ]
