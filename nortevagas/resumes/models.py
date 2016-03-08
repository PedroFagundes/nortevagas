# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify

from authentication.models import Account


class Resume(models.Model):
	account = models.ForeignKey(Account)

	last_position = models.CharField('Última profissão', max_length=50, null=True, blank=True)
	skills = models.CharField('Competências', max_length=150, null=True, blank=True)
	about = models.TextField('Sobre', max_length=500, null=False, blank=False)

	slug = models.SlugField(blank=True, max_length=100, unique=True)

	def __unicode__(self):
		return self.account.name

	class Meta:
		verbose_name='Currículo'
		verbose_name_plural='Currículos'

	def save(self):
		slug = u"curriculo de-"+self.account.name
		self.slug = slugify(slug)
		super(Resume, self).save()

	def split_skills(self):
		return self.skills.split(",")


class Education(models.Model):
	resume = models.ForeignKey(Resume, related_name='education_of_resume')
	school_name = models.CharField('Instituição de ensino', max_length=50, blank=False, null=False)
	qualification = models.CharField('Qualificação', max_length=50, blank=False, null=False)
	start_end_date = models.CharField('Data de início e término', max_length=30, blank=False, null=False)
	notes = models.TextField('Observações', max_length=500, blank=True, null=True)

	def __unicode__(self):
		return "%s de %s na %s" % (self.qualification, self.resume.account.name, self.school_name)

	class Meta:
		verbose_name='Curso'
		verbose_name_plural='Cursos'


class Experience(models.Model):
	resume = models.ForeignKey(Resume, related_name='experience_of_resume')
	employer = models.CharField('Empresa', max_length=50, blank=False, null=False)
	job_title = models.CharField('Cargo', max_length=50, blank=False, null=False)
	start_end_date = models.CharField('Data de início e término', max_length=30, blank=False, null=False)
	notes = models.TextField('Atribuições', max_length=500, blank=True, null=True)

	def __unicode__(self):
		return "%s de %s na %s" % (self.job_title, self.resume.account.name, self.employer)

	class Meta:
		verbose_name='Experiência'
		verbose_name_plural='Experiências'
