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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.CharField(choices=[('EMPLOYEE', 'Candidato'), ('EMPLOYER', 'Empregador')], max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('street', models.CharField(max_length=50, null=True, blank=True)),
                ('number', models.SmallIntegerField(null=True, blank=True)),
                ('complement', models.CharField(max_length=20, null=True, blank=True)),
                ('neighborhood', models.CharField(max_length=20, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=9, null=True, blank=True)),
                ('city', models.CharField(max_length=30, null=True, blank=True)),
                ('state', models.CharField(max_length=20, null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('profile_picture', models.ImageField(default='uploads/profile_pictures/default.png', null=True, upload_to='uploads/profile_pictures', blank=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('groups', models.ManyToManyField(related_name='user_set', blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', blank=True, related_query_name='user', help_text='Specific permissions for this user.', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
        ),
    ]
