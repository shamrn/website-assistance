from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.views import PasswordResetCompleteView


@login_required
def dashboard(request):
    return render(request,'account/dashboard.html')


class SignUp(SuccessMessageMixin,CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_message = 'Пользователь успешно создан, вы можете войти'
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')

class PasswordResetComplet(SuccessMessageMixin,PasswordResetCompleteView):
    success_message = 'Пароль успешно восстановлен' #???