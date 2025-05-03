from django.shortcuts import render

# Create your views here.


from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView


from .models import User
from .forms import UserRegistrationForm, UserLoginForm


class RegisterView(CreateView):
    template_name = "register.html"
    model = User
    form_class = UserRegistrationForm
    success_url = "/"


class LoginPageView(LoginView):
    template_name = "login.html"
    form_class = UserLoginForm
    redirect_authenticated_user = True
    success_url = '/'
