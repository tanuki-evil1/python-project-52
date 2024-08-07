from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    authentication_form = AuthenticationForm
    template_name = 'base_form.html'
    success_message = _('You are logged in')
    next_page = reverse_lazy('index')
    extra_context = {'title': _('Login'), 'button_text': _('Enter')}


class UserLogoutView(LogoutView):
    success_message = _('You are logged out')
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
