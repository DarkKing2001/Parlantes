from django.urls import path, include

from . import views

urlpatterns = [
    path('base', views.base, name = 'base'),
    path('menu', views.menu, name = 'menu'),
    path('tipo_parlante', views.tipo_parlante, name='tipo_parlante'),
]
