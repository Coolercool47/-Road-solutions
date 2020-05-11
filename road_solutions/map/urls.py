from django.urls import path

from . import views

urlpatterns = [
    path('', views.map_choice, name='index'),
    path('map/', views.map_open, name='opened'),
    path('.', views.main, name='main'),
]

