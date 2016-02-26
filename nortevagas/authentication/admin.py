# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Account

class AccountAdmin(admin.ModelAdmin):
	list_display = ('email', 'user_type')
	list_filter = ('email', 'user_type')

admin.site.register(Account, AccountAdmin)
