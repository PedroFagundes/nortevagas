# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('user_type', models.CharField(choices=[('EMPLOYEE', 'Candidato'), ('EMPLOYER', 'Empregador')], max_length=40)),
                ('name', models.CharField(blank=True, max_length=40)),
                ('street', models.CharField(blank=True, null=True, max_length=50)),
                ('number', models.SmallIntegerField(blank=True, null=True)),
                ('complement', models.CharField(blank=True, null=True, max_length=20)),
                ('neighborhood', models.CharField(blank=True, null=True, max_length=20)),
                ('zip_code', models.CharField(blank=True, null=True, max_length=9)),
                ('city', models.CharField(blank=True, null=True, max_length=30)),
                ('state', models.CharField(blank=True, null=True, max_length=20)),
                ('phone', models.CharField(blank=True, null=True, max_length=20)),
                ('profile_picture', models.ImageField(blank=True, upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('pdated_at', models.DateField(auto_now=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group', related_name='user_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', to='auth.Permission', related_name='user_set', blank=True, help_text='Specific permissions for this user.', related_query_name='user')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
