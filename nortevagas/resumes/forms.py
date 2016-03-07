# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Resume, Education, Experience


class ResumeForm(ModelForm):
	class Meta:
		model = Resume

EducationFormSet = inlineformset_factory(Resume, Education)
ExperienceFormSet = inlineformset_factory(Resume, Experience)