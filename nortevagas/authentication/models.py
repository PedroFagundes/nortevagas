# -*- coding: utf-8 -*-
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin)
from django.db import models

EMPLOYEE = 'EMPLOYEE'
EMPLOYER = 'EMPLOYER'
USER_TYPE_CHOICES = (
    (EMPLOYEE, 'Candidato'),
    (EMPLOYER, 'Empregador')
)

class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError(u'O usuário deve ter um e-mail válido')

		account = self.model(
			email=self.normalize_email(email))

		account.set_password(password)
		account.save()
		return account

	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)

		account.is_superuser = True
		account.is_staff = True
		account.save()
		return account


class Account(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	user_type = models.CharField(
		choices=USER_TYPE_CHOICES,
		max_length=40,
		blank=False,
		null=False)
	name = models.CharField(max_length=40, blank=True)

	street = models.CharField(max_length=50, blank=True, null=True)
	number = models.SmallIntegerField(blank=True, null=True)
	complement = models.CharField(max_length=20, blank=True, null=True)
	neighborhood = models.CharField(max_length=20, blank=True, null=True)
	zip_code = models.CharField(max_length=9, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)
	state = models.CharField(max_length=20, blank=True, null=True)

	phone = models.CharField(max_length=20, blank=True, null=True)
	profile_picture = models.ImageField(
		null=True,
		blank=True,
		upload_to='uploads/profile_pictures',
		default='uploads/profile_pictures/default.png')

	is_staff = models.BooleanField(default=False)
	created_at = models.DateField(auto_now_add=True)
	pdated_at = models.DateField(auto_now=True)

	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['user_type']

	class Meta:
		verbose_name = u'Usuário'
		verbose_name_plural = u'Usuários'

	def __str__(self):
		return self.name()

	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name.split(" ")[0]

	def get_full_address(self):
		return '%s %s %s, %s - %s ' % (
			self.street, str(self.number), self.complement,
			self.neighborhood, self.city)