# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Experi\xeancia', 'verbose_name_plural': 'Experi\xeancias'},
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Curr\xedculo', 'verbose_name_plural': 'Curr\xedculos'},
        ),
    ]
