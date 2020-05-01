from django.urls import path
from . import views


app_name = 'vacancy'
urlpatterns = [
    path('', views.VacancyView.as_view()),
]
