# -*- coding: utf-8 -*-
from datetime import datetime

from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.clickjacking import xframe_options_sameorigin

from pure_pagination.mixins import PaginationMixin


from .models import Job, JobApplication, JobBookmark
from .forms import JobCreateForm, JobSearchForm, JobApplicationEmployerUpdateForm


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


class JobSearchView(PaginationMixin, ListView):
    model = Job
    form_class = JobSearchForm
    context_object_name = 'jobs'
    template_name = 'jobs/job-search.html'
    paginate_by = 3
    object = Job

    def get_context_data(self, **kwargs):
        context = super(JobSearchView, self).get_context_data(**kwargs)
        if self.request.GET['keywords'] != '':
            context['jobs'] = Job.objects.filter(Q(title__icontains=self.request.GET['keywords']) | Q(keywords__icontains=self.request.GET['keywords']) | Q(employer__name__icontains=self.request.GET['keywords']))
            context['search_terms'] = self.request.GET['keywords']
        else:
            pass
        return context

    # def get_queryset(self):
    #     import pdb; pdb.set_trace()
    #     if self.request.GET['keywords']:
    #         return Job.objects.filter(Q(title__icontains=self.request.GET['keywords']) | Q(keywords__icontains=self.request.GET['keywords']) | Q(employer__name__icontains=self.request.GET['keywords']))
    #     return Job.objects.filter(active=True, expiration_date__gte=datetime.now()).order_by('-post_date')
    #     qs = super(JobSearchView, self).get_queryset()
    #     return qs.filter(keywords__icontains=self.kwargs['keywords'])

    # def get_context_data(self, **kwargs):
    #     context = super(JobSearchView, self).get_context_data(**kwargs)

    #     search_text = ""   #Assume no search

    #     if(self.request.method == "GET"):
    #         search_text = self.request.GET.get("search_text", "").strip().lower()

    #     if(search_text != ""):
    #         job_search_results = Job.objects.filter(name__icontains=search_text)
    #     else:
    #         job_search_results = []

    #     context["search_text"] = search_text
    #     context["job_search_results"] = job_search_results

    #     return  context


class ManageJobsView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/manage-jobs.html'

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user.pk, active=True, expiration_date__gte=datetime.now())


class ManageJobApplicationsView(ListView):
    model = JobApplication
    context_object_name = 'job_applications'
    template_name = 'jobs/manage-job-applications.html'

    def get_queryset(self):
        return JobApplication.objects.filter(job__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ManageJobApplicationsView, self).get_context_data(**kwargs)
        context['form'] = JobApplicationEmployerUpdateForm
        return context


@xframe_options_sameorigin
def toggle_job_filled(request, job_id):
    job = None
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist as e:
        raise  ValueError("Unknown job.id=" + str(job_id) + ". Original error: " + str(e))

    if job.employer == request.user:
        job.filled = not job.filled
        job.save()
    else:
        raise ValueError("Você nao tem permissão de alterar esta vaga")

    return  HttpResponseRedirect(reverse_lazy('manage_jobs'))

@xframe_options_sameorigin
def toggle_job_active(request, job_id):
    job = None
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist as e:
        raise ValueError("Unknown job.id=" + str(job_id) + ". Original error: " + str(e))

    job.active = not job.active
    job.save()

    return HttpResponseRedirect(reverse_lazy('manage_jobs'))

@xframe_options_sameorigin
def bookmark_job(request, job_id):
    job = None
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist as e:
        raise ValueError("Unknown job.id=" + str(job_id) + ". Original error: " + str(e))

    JobBookmark.objects.create(job=job, candidate=request.user)

    return HttpResponseRedirect(reverse_lazy('home')) # Depois de marcar uma vaga, o usuario será direcionado para as vagas que ele marcou "JobApplicationList"

@xframe_options_sameorigin
def job_application_employer_update(request, application_id):
    import pdb; pdb.set_trace()
    application = None
    try:
        application = JobApplication.objects.get(pk=application_id)
    except JobApplication.DoesNotExist as e:
        raise ValueError("Unknown application.id=" + str(application_id) + ". Original error: " + str(e))

    application.employer_note =request.POST['employer_note']
    application.save()

    return HttpResponseRedirect(reverse_lazy('manage_jobs'))
