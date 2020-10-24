from django.urls import path, incluide

from . import views

urlpatterns = [
    path('base/', views.base, name = 'base'),
]
