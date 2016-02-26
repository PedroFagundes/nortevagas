# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from datetime import datetime

from jobs.models import Job


class Home(TemplateView):
    template_name = 'homesite/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['jobs_total'] = len(Job.objects.all())
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
