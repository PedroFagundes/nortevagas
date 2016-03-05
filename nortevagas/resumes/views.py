# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView

from pure_pagination.mixins import PaginationMixin

from .models import Resume, Education, Experience


class ResumeDetailView(DetailView):
	model = Resume
	template_name = 'resumes/resume-detail.html'

	def get_context_data(self, **kwargs):
		context = super(ResumeDetailView, self).get_context_data(**kwargs)
		context['educations'] = Education.objects.filter(resume=context['resume'])
		context['experiences'] = Experience.objects.filter(resume=context['resume'])
		return context


class ResumeSearchView(PaginationMixin, ListView):
	model = Resume
	context_object_name = 'resumes'
	template_name = 'resumes/resumes-search.html'
	paginate_by = 10
	object = Resume

	def get_context_data(self, **kwargs):
		context = super(ResumeSearchView, self).get_context_data(**kwargs)
		try:
			context['resumes'] = Resume.objects.filter(skills__icontains=self.request.GET['keywords'])
			context['search_term'] = self.request.GET['keywords']
		except:
			pass
		return context
