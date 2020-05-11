from django.urls import path
from . import views

urlpatterns = [
    path('', views.description, name='index'),
    path('.', views.main, name='main'),
]
