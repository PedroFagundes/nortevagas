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
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
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
            options={
                'verbose_name': 'Experi\xeancia',
                'verbose_name_plural': 'Experi\xeancias',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_position', models.CharField(max_length=50, null=True, verbose_name=b'\xc3\x9altima profiss\xc3\xa3o', blank=True)),
                ('skills', models.CharField(max_length=150, null=True, verbose_name=b'Compet\xc3\xaancias', blank=True)),
                ('about', models.TextField(max_length=500, verbose_name=b'Sobre')),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curr\xedculo',
                'verbose_name_plural': 'Curr\xedculos',
            },
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
