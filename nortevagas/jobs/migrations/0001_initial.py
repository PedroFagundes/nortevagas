# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='T\xedtulo')),
                ('keywords', models.CharField(max_length=50, verbose_name='Palavras-chave')),
                ('description', models.TextField(max_length=500, verbose_name='Descri\xe7\xe3o')),
                ('employer_logo', models.ImageField(default=b'employer-logos/default-logo.jpg', upload_to=b'employer-logos/')),
                ('city', models.CharField(max_length=30, verbose_name='Cidade')),
                ('salary', models.CharField(max_length=15, verbose_name='Sal\xe1rio')),
                ('benefits', models.CharField(max_length=150, null=True, verbose_name='Benef\xedcios', blank=True)),
                ('job_address', models.CharField(max_length=150, verbose_name=b'Local de trabalho')),
                ('expedient', models.CharField(max_length=30, verbose_name=b'Expediente')),
                ('category', models.CharField(max_length=150, verbose_name=b'Categoria')),
                ('job_type', models.CharField(max_length=35, verbose_name=b'Tipo de vaga', choices=[(b'ESTAGIO', b'Est\xc3\xa1gio'), (b'TREINEE', b'Treinee'), (b'INTEGRAL', b'Integral'), (b'MEIO EXPEDIENTE', b'Meio Expediente')])),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('hired', models.BooleanField(default=False, verbose_name=b'Ocupada')),
                ('special_job', models.BooleanField(default=False)),
                ('sponsored', models.BooleanField(default=False)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField(default=datetime.datetime(2016, 3, 26, 21, 52, 11, 562201))),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
    ]
