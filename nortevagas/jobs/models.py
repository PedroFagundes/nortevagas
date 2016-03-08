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

JOB_CATEGORY_CHOICES = [
	('ADMINISTRATIVO', 'Administrativo'),
	('ALIMENTOS', 'Alimentos'),
	('COMERCIO', 'Comércio'),
	('CONSTRUCAO', 'Construção'),
	('CONTABILIDADE', 'Contabilidade'),
	('EDUCACAO', 'Educação'),
	('FINANCEIRO', 'Financeiro'),
	('INFORMATICA', 'Informática'),
	('JURIDICO', 'Jurídico'),
	('LIMPEZA', 'Limpeza'),
	('LOGISTICA', 'Logística'),
	('MANUTENCAO', 'Manutenção'),
	('MARKETING', 'Marketing'),
	('MECANICO', 'Mecânico'),
	('PRODUCAO', 'Produção'),
	('RECURSOS_HUMANOS', 'Recursos Humanos'),
	('SAUDE', 'Saúde'),
	('SEGURANCA', 'Segurança'),
	('SERVICOS_DOMESTICOS', 'Serviços Domésticos'),
	('SERVICOS_PESSOAIS', 'Serviços Pessoais'),
]

JOB_APPLICATION_STATUS_CHOICES = [
	('NEW', 'Nova'),
	('INTERVIEWED', 'Entrevistado'),
	('HIRED', 'Contratado'),
	('ARCHIVED', 'Arquivado'),
]

JOB_APPLICATION_RATING_CHOICES = [
	(0, 0),
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
]


def get_expiration_date():
	return datetime.today() + timedelta(days=30)


class Job(models.Model):
	employer = models.ForeignKey(Account)
	title = models.CharField(u'Título', max_length=100, null=False, blank=False)
	keywords = models.CharField(u'Palavras-chave', max_length=50, null=False, blank=False)
	job_position = models.CharField(u'Cargo', max_length=50, null=False, blank=False)
	description = models.TextField(u'Descrição', max_length=500, null=False, blank=False)
	city = models.CharField(u'Cidade', max_length=30, null=False, blank=False)
	salary = models.CharField(u'Salário', max_length=25, null=False, blank=False)
	responsabilities = models.CharField(u'Responsabilidades', max_length=250, null=True, blank=True)
	requirements = models.CharField(u'Requisitos do candidato', max_length=250, null=True, blank=True)
	benefits = models.CharField(u'Benefícios', max_length=150, null=True, blank=True)
	# employer_logo = models.ImageField('Logomarca da empresa', upload_to='employer-logos/', default='employer-logos/default-logo.png')
	expedient = models.CharField(u'Carga Horária', max_length=30, null=False, blank=False)
	category = models.CharField(u'Categoria', max_length=150, null=False, blank=False, choices = JOB_CATEGORY_CHOICES)
	job_type = models.CharField(u'Tipo de vaga', max_length=35, null=False, blank=False, choices=JOB_TYPE_CHOICES)
	slug = models.SlugField(blank=True, max_length=250, unique=True)

	active = models.BooleanField(u'Ativa', default=True)
	filled = models.BooleanField(u'Ocupada', default=False)
	special_job = models.BooleanField(u'Vaga para deficientes', default=False)
	sponsored = models.BooleanField(u'Patrocinada', default=False)

	post_date = models.DateField(auto_now_add=True)
	expiration_date = models.DateField(default=get_expiration_date)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = 'Vaga'
		verbose_name_plural = 'Vagas'

	def save(self):
		slug = self.title+" na area "+self.category+" em "+self.city+" por "+self.employer.name
		self.slug = slugify(slug)
		super(Job, self).save()

	def split_keywords(self):
		return self.keywords.split(",")

	def split_responsabilities(self):
		return self.responsabilities.split(",")

	def split_requirements(self):
		return self.requirements.split(",")

	def split_benefits(self):
		return self.benefits.split(",")

	def get_job_candidates(self):
		return JobApplication.objects.filter(job=self.pk)

	def is_bookmarked(self, user):
		try:
			bookmark = JobBookmark.objects.get(job=self.pk, candidate=user)
			return True
		except:
			return False


class JobApplication(models.Model):
	job = models.ForeignKey('Job')
	candidate = models.ForeignKey(Account)

	candidate_cover_letter = models.TextField(max_length=500, blank=True, null=True)

	status = models.CharField(max_length=25, default='NEW', choices=JOB_APPLICATION_STATUS_CHOICES)
	employer_note = models.TextField(max_length=500, blank=True, null=True)
	rating = models.SmallIntegerField(default=0, choices=JOB_APPLICATION_RATING_CHOICES)

	application_date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s - %s"%(self.job, self.candidate)

	class Meta:
		verbose_name = 'Candidato'
		verbose_name_plural = 'Candidatos'
		unique_together = ('job', 'candidate')


class JobBookmark(models.Model):
	job = models.ForeignKey(Job)
	candidate = models.ForeignKey(Account)

	def __unicode__(self):
		return "%s - %s" % (self.candidate, self.job)

	class Meta:
		verbose_name = "Vaga favorita de Usuario"
		verbose_name_plural = "Vagas favoritas de Usuarios"
		unique_together = ('job', 'candidate')
