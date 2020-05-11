from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_data, name='index'),
    path('.', views.main, name='main'),
]