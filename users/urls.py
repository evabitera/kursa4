from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import RegisterView, MyLogoutView, MyLoginView, email_verification
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
]