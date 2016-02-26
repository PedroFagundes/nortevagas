# -*- coding: utf-8 -*-
from django.views.generic import DetailView

from .models import Job


class JobDetail(DetailView):
    model = Job
    template_name = 'jobs/job-detail.html'
