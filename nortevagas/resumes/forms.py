# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory

from .models import Resume, Education, Experience


class ResumeForm(forms.ModelForm):
	class Meta:
		model = Resume
		fields = '__all__'
		exclude = ['slug']
		widgets = {
		'account': forms.Select(attrs={
			'style': 'display:none'
			}),
		'last_position': forms.TextInput(attrs={
			'placeholder': 'Ex.: Advogado'
			}),
		'skills': forms.TextInput(attrs={
			'placeholder': 'Ex.: leis trabalhistas, direitos do trabalhado'
			}),
		'about': forms.Textarea(attrs={
			'placeholder': 'Fale um pouco sobre você para as pessoas :)'
			}),
		}

EducationFormSet = inlineformset_factory(
	Resume,
	Education,
	fields='__all__',
	extra=1)
ExperienceFormSet = inlineformset_factory(
	Resume,
	Experience,
	fields='__all__',
	extra=1)