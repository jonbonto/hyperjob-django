"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from resume.views import new_resume
from vacancy.views import new_vacancy

urlpatterns = [
    path('', views.menu, name='menu'),
    path('admin/', admin.site.urls),
    re_path(r'login/?', views.MyLoginView.as_view()),
    re_path(r'signup/?', views.MySignupView.as_view()),
    re_path(r'logout/?', views.LogoutView.as_view()),
    path('resumes/', include('resume.urls')),
    path('resume/new', new_resume),
    path('vacancies/', include('vacancy.urls')),
    path('vacancy/new', new_vacancy),
    path('home', views.home)
]
