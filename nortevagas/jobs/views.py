# -*- coding: utf-8 -*-
from datetime import datetime

from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Job
from .forms import JobCreateForm, JobSearchForm


class JobCreateView(SuccessMessageMixin, CreateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'jobs/job-create.html'
    success_url = reverse_lazy('manage_jobs')
    success_message = "Vaga cadastrada com sucesso!"

    def get_initial(self):
        return {'employer': self.request.user.id}


class JobUpdateView(SuccessMessageMixin, UpdateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'jobs/job-update.html'
    success_url = reverse_lazy('manage_jobs')
    success_message = "Vaga atualizada com sucesso!"



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


class ManageJobsView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/manage-jobs.html'

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user.pk)
