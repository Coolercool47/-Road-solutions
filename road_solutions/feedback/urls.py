from django.urls import path

from . import views

urlpatterns = [
    path('', views.report, name='index'),
    path('send/', views.write_form, name='send'),
    path('send/.', views.main, name='main'),
]
