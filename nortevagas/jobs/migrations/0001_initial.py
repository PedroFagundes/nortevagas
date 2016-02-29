# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('keywords', models.CharField(max_length=50, verbose_name='Palavras-chave')),
                ('job_position', models.CharField(max_length=50, verbose_name='Cargo')),
                ('description', models.TextField(max_length=500, verbose_name='Descrição')),
                ('city', models.CharField(max_length=30, verbose_name='Cidade')),
                ('salary', models.CharField(max_length=15, verbose_name='Salário')),
                ('responsabilities', models.CharField(max_length=150, null=True, verbose_name='Responsabilidades', blank=True)),
                ('requirements', models.CharField(max_length=150, null=True, verbose_name='Requisitos do candidato', blank=True)),
                ('expedient', models.CharField(max_length=30, verbose_name='Expediente')),
                ('category', models.CharField(max_length=150, verbose_name='Categoria')),
                ('job_type', models.CharField(choices=[('INTEGRAL', 'Integral'), ('MEIO EXPEDIENTE', 'Meio Expediente'), ('ESTAGIO', 'Estágio'), ('TREINEE', 'Treinee')], max_length=35, verbose_name='Tipo de vaga')),
                ('slug', models.SlugField(max_length=100, unique=True, blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Ativa')),
                ('hired', models.BooleanField(default=False, verbose_name='Ocupada')),
                ('special_job', models.BooleanField(default=False, verbose_name='Vaga para deficientes')),
                ('sponsored', models.BooleanField(default=False, verbose_name='Patrocinada')),
                ('post_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField(default=datetime.datetime(2016, 3, 30, 14, 27, 21, 7686))),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vagas',
                'verbose_name': 'Vaga',
            },
        ),
    ]
