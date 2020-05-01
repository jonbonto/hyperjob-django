from django.core.exceptions import PermissionDenied, ValidationError
from django.db import DatabaseError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from . models import Resume
from django.contrib.auth.models import User

from .forms import NewResumeForm


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        _resumes = Resume.objects.all()
        return render(request, 'resumes/index.html', context={'resumes': _resumes})


def new_resume(request):
    if not request.user.is_authenticated or request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewResumeForm(request.POST)
        author = request.user
        if form.is_valid():
            description = form.cleaned_data['description']
            if not description:
                raise ValidationError
            try:
                Resume.objects.create(author=author, description=description)
                return HttpResponseRedirect('/home')
            except DatabaseError:
                raise PermissionDenied
