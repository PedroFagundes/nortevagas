# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import JobDetail

urlpatterns = [
    url(r'^(?P<slug>[^\.]+)$', JobDetail.as_view(), name='job_detail'),
]