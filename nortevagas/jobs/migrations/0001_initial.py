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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('keywords', models.CharField(max_length=50, verbose_name='Palavras-chave')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição')),
                ('city', models.CharField(max_length=30, verbose_name='Cidade')),
                ('salary', models.CharField(max_length=15, verbose_name='Salário')),
                ('benefits', models.CharField(max_length=150, verbose_name='Benefícios')),
                ('job_address', models.CharField(max_length=150, verbose_name='Local de trabalho')),
                ('expedient', models.CharField(max_length=30, verbose_name='Expediente')),
                ('hired', models.BooleanField(verbose_name='Ocupada', default=False)),
                ('category', models.CharField(max_length=150, verbose_name='Categoria')),
                ('job_type', models.CharField(choices=[('ESTAGIO', 'Estágio'), ('TREINEE', 'Treinee'), ('INTEGRAL', 'Integral'), ('MEIO EXPEDIENTE', 'Meio Expediente')], verbose_name='Tipo de vaga', max_length=35)),
                ('special_job', models.BooleanField(default=False)),
                ('sponsored', models.BooleanField(default=False)),
                ('expiration_date', models.DateField(default=datetime.datetime(2016, 3, 26, 17, 34, 53, 876032))),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
    ]
