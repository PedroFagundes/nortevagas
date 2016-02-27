# -*- coding: utf-8 -*-
from django import forms

from .models import Job


class JobSearchForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('keywords',)
        widgets = {
            'keywords': forms.TextInput(attrs={
                'placeholder': 'titulo da vaga, palavra-chave ou nome da empresa'
            }),
        }