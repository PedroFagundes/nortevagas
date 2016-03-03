# -*- coding: utf-8 -*-
from django import forms

from authentication.models import Account

from .models import Job


class JobCreateForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = '__all__'
		exclude = ['expiration_date']
		widgets = {
		'employer': forms.Select(attrs={
			'style': 'display:none'
			}),
		'title': forms.TextInput(attrs={
			'placeholder': 'Ex.: Recepcionista consultório odontológico'
			}),
		'job_type': forms.Select(attrs={
			'class': 'chosen-select-no-single',
			}),
		'category': forms.Select(attrs={
			'class': 'chosen-select',
			}),
		'keywords': forms.TextInput(attrs={
			'placeholder': 'Ex.: secretaria, consultorio, recepcionista'
			}),
		'description': forms.Textarea(attrs={
			'placeholder': 'Ex.: Buscamos secretária com experiência para vaga de recepcionista em consultório odontologico.'
			}),
		'salary': forms.TextInput(attrs={
			'placeholder': 'Ex.: R$1.050,00 ou "A combinar"'
			}),
		'city': forms.TextInput(attrs={
			'placeholder': 'Ex.: Montes Claros'
			}),
		'job_position': forms.TextInput(attrs={
			'placeholder': 'Ex.: Recepcionista'
			}),
		'responsabilities': forms.TextInput(attrs={
			'placeholder': 'Ex.: Atendimento aos pacientes, Agendamento de consultas, Remarcação, Envio de e-mails para os clientes'
			}),
		'requirements': forms.TextInput(attrs={
			'placeholder': 'Ex.: Experiência de pelo menos 6 meses com atendimento, Manuseio de computador, internet, Microsoft Word'
			}),
		'expedient': forms.TextInput(attrs={
			'placeholder': 'Ex.: 8h'
			}),
		}


class JobSearchForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('keywords',)
        widgets = {
            'keywords': forms.TextInput(attrs={
                'placeholder': 'titulo da vaga, palavra-chave ou nome da empresa'
            }),
        }