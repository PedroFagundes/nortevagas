# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import JobDetailView, JobSearchView

urlpatterns = [
    url(r'^(?P<slug>[^\.]+)$', JobDetailView.as_view(), name='job_detail'),
    url(r'^(?P<keywords>)$', JobSearchView.as_view(), name='search_job'),
]