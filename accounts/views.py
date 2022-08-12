# Django's imports
from django.shortcuts import render, redirect

# Developer's imports
from django.views import generic
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Forms' imports
from .forms import *

# Models' imports
from .models import CustomUser


# This class makes a form to subscribed new users
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm  # This form is used to create new users
    template_name = 'registration/signup.html'

    # This function redirect to login url when the new user is created
    def get_success_url(self):
        return reverse('login')


# This class makes a form to update users
class UserUpdateView(UpdateView):
    model = CustomUser
    # form_class = CustomUserChangeForm  # This form is used to update users
    template_name = 'registration/userupdate.html'
    fields = ['email',]

    # This function redirect to login url when the user was updated
    def get_success_url(self):
        return reverse('login')
