from django.urls import path, include

from . import views

urlpatterns = [
    path('base/', views.base, name = 'base'),
    path('inicio/', views.inicio, name = 'inicio'),
]
