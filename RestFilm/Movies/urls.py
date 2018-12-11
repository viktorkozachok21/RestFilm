from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('film/<slug>', views.watch, name="watch"),
    path('<slug>', views.filter, name="filter"),
    path('account/login', views.signin, name="signin"),
    path('account/registration', views.signup, name="signup"),
    path('account/logout', views.userlogout, name="userlogout"),
    path('contact/send', views.contact, name="contact"),
]
