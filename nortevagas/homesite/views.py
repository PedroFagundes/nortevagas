# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView

from jobs.models import Job


class Home(TemplateView):
    template_name = 'homesite/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.filter(sponsored=False).order_by('-post_date')
        context['sponsored_jobs'] = Job.objects.filter(sponsored=True).order_by('-post_date')
        return context
