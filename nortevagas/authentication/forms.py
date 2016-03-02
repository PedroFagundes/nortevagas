# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Account


class AccountLoginForm(AuthenticationForm):
	class Meta:
		model = Account
		fields = ('email', 'password')
		widgets = {
			'password': forms.TextInput(attrs={
				'type': 'password',
				})
		}

class AccountCreateForm(forms.ModelForm):
	name = forms.CharField(error_messages={'required': 'Diga-nos o seu nome ;D'})
	email = forms.CharField(error_messages={'required': 'Precisamos do seu melhor e-mail para te identificar. Não vamos mandar spam, tbm odiamos eles :D'})
	password = forms.CharField(error_messages={'required': 'Você nao quer criar uma conta sem senha não é mesmo!? :O'})
	# user_type = forms.ChoiceField(choices=Account.user_type.choices, error_messages={'required': 'Você quer contratar alguem ou quer achar a vaga perfeita pra você? Selecione uma opção acima'})
	class Meta:
		model = Account
		fields = ('email', 'name', 'password', 'user_type')
		widgets = {
			'password': forms.TextInput(attrs={
				'type': 'password',
				})
		}