# -*- coding: utf-8 -*-
from django import forms

from .models import Job


class JobCreateForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = '__all__'
		widgets = {
		'job_type': forms.Select(attrs={
			'class': 'chosen-select-no-single',
			}),
		'category': forms.Select(attrs={
			'class': 'chosen-select',
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