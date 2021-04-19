from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.views import PasswordResetCompleteView
from worker.models import Worker


@login_required
def dashboard(request):
    if 'redirect_login' in request.session:
        redirect_ = str(*request.session['redirect_login'])
        del request.session['redirect_login']
        return redirect(redirect_)
    profile = CustomUser.objects.get(username=request.user)
    if profile.status == 'assistant':
        worker = Worker.objects.filter(user=request.user)
    else:
        worker = False
    return render(request, 'account/dashboard.html', {'profile': profile, 'worker': worker})


class SignUp(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_message = 'Пользователь успешно создан, вы можете войти'
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')


class PasswordResetComplet(SuccessMessageMixin, PasswordResetCompleteView):
    success_message = 'Пароль успешно восстановлен'  # ???
