# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import LoginView, AccountCreateView

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', 'authentication.views.logout', name='logout'),
    url(r'^registrar/', AccountCreateView.as_view(), name='register')
]
