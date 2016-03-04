# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import (
	JobCreateView,
	JobUpdateView,
	JobDetailView,
	JobSearchView,
	ManageJobsView,
    ManageJobApplicationsView)

urlpatterns = [
    url(r'^gerenciar/$', login_required(ManageJobsView.as_view()), name='manage_jobs'),
    url(r'^nova/$', login_required(JobCreateView.as_view()), name='post_job'),
    url(r'^editar/(?P<slug>[^\.]+)$', login_required(JobUpdateView.as_view()), name='update_job'),
    url(r'^ocupar/(?P<job_id>\d+)/$', 'jobs.views.toggle_job_filled', name='toggle_job_filled'),
    url(r'^remover/(?P<job_id>\d+)/$', 'jobs.views.toggle_job_active', name='toggle_job_active'),
    url(r'^bookmark/(?P<job_id>\d+)/$', 'jobs.views.bookmark_job', name='bookmark_job'),
    url(r'^atualizar_candidatura/(?P<application_id>\d+)/$', 'jobs.views.job_application_employer_update', name='job_application_employer_update'),
    url(r'^candidatos/(?P<slug>[^/.]+)$', login_required(ManageJobApplicationsView.as_view()), name='manage_job_applications'),
    url(r'^pesquisar/$', JobSearchView.as_view(), name='search_job'),
    url(r'^(?P<slug>[^\.]+)$', JobDetailView.as_view(), name='job_detail'),
]