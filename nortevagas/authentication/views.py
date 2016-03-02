# -*- coding: utf-8 -*-
from django.views.generic import FormView, CreateView
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.utils.decorators import method_decorator
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .models import Account
from .forms import AccountLoginForm, AccountCreateForm


class LoginView(FormView):
	form_class = AccountLoginForm
	template_name = 'authentication/login.html'

	@method_decorator(sensitive_post_parameters('password'))
	def dispatch(self, request, *args, **kwargs):
		request.session.set_test_cookie()
		return super(LoginView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		if self.request.POST['next']:
			redirect_to = self.request.POST['next']
		else:
			redirect_to = settings.LOGIN_REDIRECT_URL
		auth_login(self.request, form.get_user())
		authenticate(username=form.cleaned_data.get('username'),
					 password=form.cleaned_data.get('password'))
		if self.request.session.test_cookie_worked():
			self.request.session.delete_test_cookie()
			return HttpResponseRedirect(redirect_to)

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))


class AccountCreateView(CreateView):
	model = Account
	form_class = AccountCreateForm
	template_name = 'authentication/register.html'

	def post(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class(request.POST)
		if form.is_valid():
			new_account = Account.objects.create_user(**form.cleaned_data)
			Account.backend = 'django.contrib.auth.backends.ModelBackend'
			auth_login(request, new_account)
			messages.success(self.request, "Usuário cadastrado com sucesso!")
			return HttpResponseRedirect(reverse_lazy('home'))
		else:
			return self.render_to_response(self.get_context_data(form=form))


def logout(request):
	auth_logout(request)
	return redirect('/')