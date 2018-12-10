from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('film/<slug>', views.watch, name="watch"),
    path('<slug>', views.filter, name="filter"),
]
