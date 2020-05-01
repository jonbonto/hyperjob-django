from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView

from resume.forms import NewResumeForm
from vacancy.forms import NewVacancyForm

def menu(request):
    return render(request, 'index.html')


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'signup.html'


def home(request):
    if not request.user.is_authenticated:
        return redirect(to='/login')
    form = NewResumeForm()
    action = '/resume/new'
    if request.user.is_staff:
        form = NewVacancyForm()
        action = '/vacancy/new'
    return render(request, 'home.html', {'form': form, 'action': action})
