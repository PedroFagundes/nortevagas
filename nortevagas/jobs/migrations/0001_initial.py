# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jobs.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='T\xedtulo')),
                ('keywords', models.CharField(max_length=50, verbose_name='Palavras-chave')),
                ('job_position', models.CharField(max_length=50, verbose_name='Cargo')),
                ('description', models.TextField(max_length=500, verbose_name='Descri\xe7\xe3o')),
                ('city', models.CharField(max_length=30, verbose_name='Cidade')),
                ('salary', models.CharField(max_length=15, verbose_name='Sal\xe1rio')),
                ('responsabilities', models.CharField(max_length=150, null=True, verbose_name='Responsabilidades', blank=True)),
                ('requirements', models.CharField(max_length=150, null=True, verbose_name='Requisitos do candidato', blank=True)),
                ('expedient', models.CharField(max_length=30, verbose_name='Carga Hor\xe1ria')),
                ('category', models.CharField(max_length=150, verbose_name='Categoria', choices=[(b'ADMINISTRATIVO', b'Administrativo'), (b'ALIMENTOS', b'Alimentos'), (b'COMERCIO', b'Com\xc3\xa9rcio'), (b'CONSTRUCAO', b'Constru\xc3\xa7\xc3\xa3o'), (b'CONTABILIDADE', b'Contabilidade'), (b'EDUCACAO', b'Educa\xc3\xa7\xc3\xa3o'), (b'FINANCEIRO', b'Financeiro'), (b'INFORMATICA', b'Inform\xc3\xa1tica'), (b'JURIDICO', b'Jur\xc3\xaddico'), (b'LIMPEZA', b'Limpeza'), (b'LOGISTICA', b'Log\xc3\xadstica'), (b'MANUTENCAO', b'Manuten\xc3\xa7\xc3\xa3o'), (b'MARKETING', b'Marketing'), (b'MECANICO', b'Mec\xc3\xa2nico'), (b'PRODUCAO', b'Produ\xc3\xa7\xc3\xa3o'), (b'RECURSOS_HUMANOS', b'Recursos Humanos'), (b'SAUDE', b'Sa\xc3\xbade'), (b'SEGURANCA', b'Seguran\xc3\xa7a'), (b'SERVICOS_DOMESTICOS', b'Servi\xc3\xa7os Dom\xc3\xa9sticos'), (b'SERVICOS_PESSOAIS', b'Servi\xc3\xa7os Pessoais')])),
                ('job_type', models.CharField(max_length=35, verbose_name='Tipo de vaga', choices=[(b'INTEGRAL', b'Integral'), (b'MEIO EXPEDIENTE', b'Meio Expediente'), (b'ESTAGIO', b'Est\xc3\xa1gio'), (b'TREINEE', b'Treinee')])),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Ativa')),
                ('filled', models.BooleanField(default=False, verbose_name='Ocupada')),
                ('special_job', models.BooleanField(default=False, verbose_name='Vaga para deficientes')),
                ('sponsored', models.BooleanField(default=False, verbose_name='Patrocinada')),
                ('post_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField(default=jobs.models.get_expiration_date)),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidate_cover_letter', models.TextField(max_length=500, null=True, blank=True)),
                ('status', models.CharField(default=b'NEW', max_length=25, choices=[(b'NEW', b'Nova'), (b'INTERVIEWED', b'Entrevistado'), (b'HIRED', b'Contratado'), (b'ARCHIVED', b'Arquivado')])),
                ('employer_note', models.TextField(max_length=500, null=True, blank=True)),
                ('rating', models.SmallIntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('application_date', models.DateField(auto_now_add=True)),
                ('candidate', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(to='jobs.Job')),
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
            },
        ),
        migrations.CreateModel(
            name='JobBookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidate', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(to='jobs.Job')),
            ],
            options={
                'verbose_name': 'Vaga favorita de Usuario',
                'verbose_name_plural': 'Vagas favoritas de Usuarios',
            },
        ),
        migrations.AlterUniqueTogether(
            name='jobbookmark',
            unique_together=set([('job', 'candidate')]),
        ),
        migrations.AlterUniqueTogether(
            name='jobapplication',
            unique_together=set([('job', 'candidate')]),
        ),
    ]
