# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ResumeCreateView, ResumeDetailView, ResumeSearchView

urlpatterns = [
    url(r'^$', ResumeSearchView.as_view(), name='search_resume'),
    url(r'^cadastrar/$', ResumeCreateView.as_view(), name='create_resume'),
    url(r'^(?P<slug>[^\.]+)$', ResumeDetailView.as_view(), name='resume_detail'),
]