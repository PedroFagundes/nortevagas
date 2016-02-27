# -*- coding: utf-8 -*-
from datetime import datetime

from django.views.generic import DetailView, ListView
from django.db.models import Q

from .models import Job
from .forms import JobSearchForm


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job-detail.html'


class JobSearchView(ListView):
    model = Job
    form_class = JobSearchForm
    context_object_name = 'jobs'
    template_name = 'jobs/job-search.html'

    def get_queryset(self):
        import pdb; pdb.set_trace()
        if self.request.GET['keywords']:
            return Job.objects.filter(Q(title__icontains=self.request.GET['keywords']) | Q(keywords__icontains=self.request.GET['keywords']) | Q(employer__name__icontains=self.request.GET['keywords']))
        return Job.objects.filter(active=True, expiration_date__gte=datetime.now()).order_by('-post_date')
        # qs = super(JobSearchView, self).get_queryset()
        # return qs.filter(keywords__icontains=self.kwargs['keywords'])
