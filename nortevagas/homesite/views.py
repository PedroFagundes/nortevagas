# -*- coding: utf-8 -*-
from datetime import datetime

from django.views.generic import TemplateView, DetailView
from django.http import HttpResponseRedirect

from jobs.models import Job
from jobs.forms import JobSearchForm


class Home(TemplateView):
    template_name = 'homesite/home.html'
    form_class = JobSearchForm

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context['form'].is_valid():
            return HtppResponseRedirect('vagas/')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['jobs_total'] = len(Job.objects.all())
        context['form'] = self.form_class
        jobs = Job.objects.filter(
        	sponsored=False,
        	expiration_date__gte=datetime.now(),
        	active=True).order_by('-post_date', '-id')
        sponsored_jobs = Job.objects.filter(
        	sponsored=True,
        	expiration_date__gte=datetime.now(),
        	active=True).order_by('-post_date', '-id')
        if len(jobs) > 10:
        	context['jobs'] = jobs[:10]
        else:
        	context['jobs'] = jobs
        if len(sponsored_jobs) > 10:
        	context['sponsored_jobs'] = sponsored_jobs[:10]
        else:
        	context['sponsored_jobs'] = sponsored_jobs
        return context
