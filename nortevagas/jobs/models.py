# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify
from datetime import datetime, timedelta

from authentication.models import Account

JOB_TYPE_CHOICES = [
	('INTEGRAL', 'Integral'),
	('MEIO EXPEDIENTE', 'Meio Expediente'),
	('ESTAGIO', 'Estágio'),
	('TREINEE', 'Treinee')
]


class Job(models.Model):
	employer = models.ForeignKey(Account)
	title = models.CharField(u'Título', max_length=50, null=False, blank=False)
	keywords = models.CharField(u'Palavras-chave', max_length=50, null=False, blank=False)
	job_position = models.CharField(u'Cargo', max_length=50, null=False, blank=False)
	description = models.TextField(u'Descrição', max_length=500, null=False, blank=False)
	city = models.CharField(u'Cidade', max_length=30, null=False, blank=False)
	salary = models.CharField(u'Salário', max_length=15, null=False, blank=False)
	responsabilities = models.CharField(u'Responsabilidades', max_length=150, null=True, blank=True)
	requirements = models.CharField(u'Requisitos do candidato', max_length=150, null=True, blank=True)
	# employer_logo = models.ImageField('Logomarca da empresa', upload_to='employer-logos/', default='employer-logos/default-logo.png')
	expedient = models.CharField(u'Expediente', max_length=30, null=False, blank=False)
	category = models.CharField(u'Categoria', max_length=150, null=False, blank=False)
	job_type = models.CharField(u'Tipo de vaga', max_length=35, null=False, blank=False, choices=JOB_TYPE_CHOICES)
	slug = models.SlugField(blank=True, max_length=100, unique=True)

	active = models.BooleanField(u'Ativa', default=True)
	hired = models.BooleanField(u'Ocupada', default=False)
	special_job = models.BooleanField(u'Vaga para deficientes', default=False)
	sponsored = models.BooleanField(u'Patrocinada', default=False)

	post_date = models.DateField(auto_now_add=True)
	expiration_date = models.DateField(default=datetime.now()+timedelta(days=30))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Vaga'
		verbose_name_plural = 'Vagas'

	def save(self):
		self.slug = slugify(self.title)
		super(Job, self).save()

	def split_keywords(self):
		return self.keywords.split(",")

	def split_responsabilities(self):
		return self.responsabilities.split(",")

	def split_requirements(self):
		return self.requirements.split(",")