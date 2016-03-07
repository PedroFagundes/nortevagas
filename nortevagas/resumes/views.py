# -*- coding: utf-8 -*-
from django.views.generic import CreateView, DetailView, ListView
from django.core.urlresolvers import reverse_lazy

from pure_pagination.mixins import PaginationMixin

from .models import Resume, Education, Experience
from .forms import ResumeForm, EducationFormSet, ExperienceFormSet


class ResumeCreateView(CreateView):
	template_name = 'resumes/resume-create.html'
	model = Resume
	form_class = ResumeForm
	success_url = reverse_lazy('home')

	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		education_form = EducationFormSet()
		experience_form = ExperienceFormSet()
		# import pdb; pdb.set_trace()
		return self.render_to_response(
			self.get_context_data(
				form=form,
				education_form=education_form,
				experience_form=experience_form))

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		education_form = EducationFormSet(self.request.POST)
		experience_form = ExperienceFormSet(self.request.POST)
		if (form.is_valid() and education_form.is_valid() and experience_form.is_valid()):
			return self.form_valid(form, education_form, experience_form)
		else:
			return self.form_invalid(form, education_form, experience_form)

	def form_valid(self, form, education_form, experience_form):
		self.object = form.save()
		education_form.instance = self.object
		education_form.save()
		experience_form = self.object
		experience_form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, education_form, experience_form):
		return self.render_to_response(
			self.get_context_data(
				form=form,
				education_form=education_form,
				experience_form=experience_form))


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
