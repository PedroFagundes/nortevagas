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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Título', max_length=50)),
                ('keywords', models.CharField(verbose_name='Palavras-chave', max_length=50)),
                ('job_position', models.CharField(verbose_name='Cargo', max_length=50)),
                ('description', models.TextField(verbose_name='Descrição', max_length=500)),
                ('city', models.CharField(verbose_name='Cidade', max_length=30)),
                ('salary', models.CharField(verbose_name='Salário', max_length=15)),
                ('responsabilities', models.CharField(verbose_name='Responsabilidades', blank=True, null=True, max_length=150)),
                ('requirements', models.CharField(verbose_name='Requisitos do candidato', blank=True, null=True, max_length=150)),
                ('expedient', models.CharField(verbose_name='Expediente', max_length=30)),
                ('category', models.CharField(verbose_name='Categoria', max_length=150)),
                ('job_type', models.CharField(verbose_name='Tipo de vaga', choices=[('INTEGRAL', 'Integral'), ('MEIO EXPEDIENTE', 'Meio Expediente'), ('ESTAGIO', 'Estágio'), ('TREINEE', 'Treinee')], max_length=35)),
                ('slug', models.SlugField(blank=True, unique=True, max_length=100)),
                ('active', models.BooleanField(verbose_name='Ativa', default=True)),
                ('hired', models.BooleanField(verbose_name='Ocupada', default=False)),
                ('special_job', models.BooleanField(verbose_name='Vaga para deficientes', default=False)),
                ('sponsored', models.BooleanField(verbose_name='Patrocinada', default=False)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField(default=datetime.datetime(2016, 3, 27, 17, 7, 3, 944756))),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
    ]
