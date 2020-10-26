from django.urls import path, include

from . import views

urlpatterns = [
    path('base/', views.base, name = 'base'),
    path('inicio/', views.inicio, name = 'inicio'),
    path('tipo_parlante/', views.tipo_parlante, name='tipo_parlante'),
]
