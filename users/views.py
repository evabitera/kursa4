import random
import secrets
import string

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from users.forms import RegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http:/{host}/users/email-confirm/{token}/'
        send_mail(subject="Подтвердите почту",
                  message=f"Чтобы подтвердить почту, перейдите по ссылке {url}",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email, ]
                  )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class MyLogoutView(LogoutView):
    model = User
    form_class = RegisterForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main:mails_list')

    def logout_view(self):
        logout(self)
        return redirect("/")


class MyLoginView(LoginView):
    model = User
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main:mails_list')
