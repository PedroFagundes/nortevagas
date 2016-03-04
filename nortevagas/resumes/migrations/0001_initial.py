# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=50, verbose_name=b'Institui\xc3\xa7\xc3\xa3o de ensino')),
                ('qualification', models.CharField(max_length=50, verbose_name=b'Qualifica\xc3\xa7\xc3\xa3o')),
                ('start_end_date', models.CharField(max_length=30, verbose_name=b'Data de in\xc3\xadcio e t\xc3\xa9rmino')),
                ('notes', models.TextField(max_length=500, null=True, verbose_name=b'Observa\xc3\xa7\xc3\xb5es', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer', models.CharField(max_length=50, verbose_name=b'Empresa')),
                ('job_title', models.CharField(max_length=50, verbose_name=b'Cargo')),
                ('start_end_date', models.CharField(max_length=30, verbose_name=b'Data de in\xc3\xadcio e t\xc3\xa9rmino')),
                ('notes', models.TextField(max_length=500, null=True, verbose_name=b'Atribui\xc3\xa7\xc3\xb5es', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_position', models.CharField(max_length=50, null=True, verbose_name=b'Profiss\xc3\xa3o atual', blank=True)),
                ('content', models.TextField(max_length=500, verbose_name=b'Conte\xc3\xbado')),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('education', models.ForeignKey(related_name='resume_of_education', to='resumes.Education')),
                ('experience', models.ForeignKey(related_name='resume_of_experience', to='resumes.Experience')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(related_name='experience_of_resume', to='resumes.Resume'),
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(related_name='education_of_resume', to='resumes.Resume'),
        ),
    ]
