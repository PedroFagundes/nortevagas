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
from resumes.models import Resume


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
    paginate_by = 10

    def get_queryset(self):
        try:
            return Job.objects.filter(Q(title__icontains=self.request.GET['keywords']) | Q(keywords__icontains=self.request.GET['keywords']) | Q(employer__name__icontains=self.request.GET['keywords']))
        except:
            return Job.objects.filter(active=True, expiration_date__gte=datetime.now())

    def get_context_data(self, **kwargs):
        context = super(JobSearchView, self).get_context_data(**kwargs)
        try:
            context['search_term'] = self.request.GET['keywords']
        except:
            pass
        return context


class ManageJobsView(PaginationMixin, ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/manage-jobs.html'
    paginate_by = 5

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user.pk, active=True, expiration_date__gte=datetime.now()).order_by('-pk')


class ManageJobApplicationsView(ListView):
    model = JobApplication
    context_object_name = 'job_applications'
    template_name = 'jobs/manage-job-applications.html'

    def get_queryset(self):
        return JobApplication.objects.filter(job__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ManageJobApplicationsView, self).get_context_data(**kwargs)
        context['rating_options'] = []
        context['status_options'] = []
        for key, value in JobApplication._meta.get_field('rating').choices:
            context['rating_options'].append(key)
        for status in JobApplication._meta.get_field('status').choices:
            context['status_options'].append(status)

        return context


@xframe_options_sameorigin
def toggle_job_filled(request, job_pk):
    job = None
    try:
        job = Job.objects.get(pk=job_pk)
    except Job.DoesNotExist as e:
        raise  ValueError("Unknown job.pk=" + str(job_pk) + ". Original error: " + str(e))

    if job.employer == request.user:
        job.filled = not job.filled
        job.save()
    else:
        raise ValueError("Você nao tem permissão de alterar esta vaga")

    return  HttpResponseRedirect(reverse_lazy('manage_jobs'))

@xframe_options_sameorigin
def toggle_job_active(request, job_pk):
    job = None
    try:
        job = Job.objects.get(pk=job_pk)
    except Job.DoesNotExist as e:
        raise ValueError("Unknown job.pk=" + str(job_pk) + ". Original error: " + str(e))

    job.active = not job.active
    job.save()

    return HttpResponseRedirect(reverse_lazy('manage_jobs'))

@xframe_options_sameorigin
def bookmark_job(request, job_pk):
    job = None
    try:
        job = Job.objects.get(pk=job_pk)
    except Job.DoesNotExist as e:
        raise ValueError("Unknown job.pk=" + str(job_pk) + ". Original error: " + str(e))

    JobBookmark.objects.create(job=job, candidate=request.user)

    return HttpResponseRedirect(reverse_lazy('job_detail', kwargs={'slug': job.slug})) # Depois de marcar uma vaga, o usuario será direcionado para as vagas que ele marcou "JobApplicationList"

@xframe_options_sameorigin
def apply_to_job(request, job_pk):
    job = None
    try:
        job = Job.objects.get(pk=job_pk)
        resume = Resume.objects.get(account=request.user)
    except Job.DoesNotExist as e:
        raise ValueError("Unknown job.pk=" + str(job_pk) + ". Original error: " + str(e))
    import pdb; pdb.set_trace()

    JobApplication.objects.create(job=job, candidate=request.user, candidate_cover_letter=resume.about)

    return HttpResponseRedirect(reverse_lazy('job_detail', kwargs={'slug': job.slug})) # Depois de marcar uma vaga, o usuario será direcionado para as vagas que ele marcou "JobApplicationList"

@xframe_options_sameorigin
def job_application_employer_update(request, application_id):
    # import pdb; pdb.set_trace()
    application = None
    try:
        application = JobApplication.objects.get(pk=application_id)
    except JobApplication.DoesNotExist as e:
        raise ValueError("Unknown application.pk=" + str(application_id) + ". Original error: " + str(e))

    application.employer_note =request.POST['employer_note']
    application.status =request.POST['status']
    application.rating =request.POST['rating']
    application.save()

    return HttpResponseRedirect(reverse_lazy('manage_job_applications', kwargs={'slug': application.job.slug}))
