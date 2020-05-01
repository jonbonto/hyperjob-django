from django.core.exceptions import PermissionDenied, ValidationError
from django.db import DatabaseError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from . models import Vacancy
from .forms import NewVacancyForm
from django.contrib.auth.models import User


# def vacancies(request):
#     _vacancies = models.Vacancy.objects
#     return render(request, 'vacancy/vacancies.html', context={'vacancies': _vacancies})


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        _vacancies = Vacancy.objects.all()
        return render(request, 'vacancies/index.html', context={'vacancies': _vacancies})


def new_vacancy(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewVacancyForm(request.POST)
        author = request.user
        if form.is_valid():
            description = form.cleaned_data['description']
            if not description:
                raise ValidationError
            try:
                Vacancy.objects.create(author=author, description=description)
                return HttpResponseRedirect('/home')
            except DatabaseError:
                raise PermissionDenied
