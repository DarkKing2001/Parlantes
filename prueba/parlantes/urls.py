from django.urls import path, include

from . import views

urlpatterns = [
    path('base', views.base, name = 'base'),
    path('tipo_parlante', views.tipo_parlante, name='tipo_parlante'),
    path('menu', views.menu, name='menu'),
    path('agregar', views.agregar, name='agregar'),
    path('agregar_parlante', views.agregar_parlante, name='agregar_parlante'),
    path('boton_buscar', views.boton_buscar, name='boton_buscar'),
    path('buscar_por_nombre', views.buscar_por_nombre, name='buscar_por_nombre'),
    path('eliminar', views.eliminar, name='eliminar'),
]
