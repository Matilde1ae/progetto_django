from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
#from progetto_django.accounts.forms import CustomUser, CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        messages.success(self.request, 'Registrazione avvenuta con successo ' + self.request.user.username)
        return super().form_valid(form)