# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Job, JobApplication

class JobAdmin(admin.ModelAdmin):
	list_display = ('title', 'city')
	list_filter = ('title', 'city')

admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication)
