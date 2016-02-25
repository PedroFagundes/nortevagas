# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, timedelta

JOB_TYPE_CHOICES = [
	('ESTAGIO', 'Estágio'),
	('TREINEE', 'Treinee'),
	('INTEGRAL', 'Integral'),
	('MEIO EXPEDIENTE', 'Meio Expediente')
]


class Job(models.Model):
	title = models.CharField(u'Título', max_length=50, null=False, blank=False)
	keywords = models.CharField(u'Palavras-chave', max_length=50, null=False, blank=False)
	description = models.CharField(u'Descrição', max_length=500, null=False, blank=False)
	city = models.CharField(u'Cidade', max_length=30, null=False, blank=False)
	salary = models.CharField(u'Salário', max_length=15, null=False, blank=False)
	benefits = models.CharField(u'Benefícios', max_length=150)
	# employer = models.ForeignKey(Account, 'Empresa')
	job_address = models.CharField('Local de trabalho', max_length=150, null=False, blank=False)
	expedient = models.CharField('Expediente', max_length=30, null=False, blank=False)
	hired = models.BooleanField('Ocupada', default=False)
	category = models.CharField('Categoria', max_length=150, null=False, blank=False)
	job_type = models.CharField('Tipo de vaga', max_length=35, null=False, blank=False, choices=JOB_TYPE_CHOICES)

	special_job = models.BooleanField(default=False)
	sponsored = models.BooleanField(default=False)

	expiration_date = models.DateField(default=datetime.now()+timedelta(days=30))

	def __unicode__(self):
		return '%s da %s'%(self.title, self.employer)

	class Meta:
		verbose_name = 'Vaga'
		verbose_name_plural = 'Vagas'