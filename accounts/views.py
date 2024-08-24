from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
