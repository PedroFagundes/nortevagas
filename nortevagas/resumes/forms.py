# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Resume, Education, Experience


class ResumeForm(ModelForm):
	class Meta:
		model = Resume
		fields = '__all__'

EducationFormSet = inlineformset_factory(Resume, Education, fields='__all__')
ExperienceFormSet = inlineformset_factory(Resume, Experience, fields='__all__')