# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import (
	JobCreateView,
	JobUpdateView,
	JobDetailView,
	JobSearchView,
	ManageJobsView)

urlpatterns = [
    url(r'^gerenciar/$', login_required(ManageJobsView.as_view()), name='manage_jobs'),
    url(r'^nova/$', login_required(JobCreateView.as_view()), name='post_job'),
    url(r'^editar/(?P<slug>[^\.]+)$', login_required(JobUpdateView.as_view()), name='update_job'),
    url(r'^(?P<slug>[^\.]+)$', JobDetailView.as_view(), name='job_detail'),
    url(r'^(?P<keywords>)$', JobSearchView.as_view(), name='search_job'),
]